"""
SIMPLE CI: Dead simple CI/CD pipeline executor.
author: François Sevestre
email: francois.sevestre.35@gmail.com

This modules contains functions.
"""
###########################################
import sys
import os
import time
from subprocess import PIPE, STDOUT, run
from datetime import datetime

import yaml

from simple_cicd.ci_files import \
        EXAMPLE_FILE_DATA,       \
        PRE_COMMIT_HOOK,         \
        PRE_COMMIT_HOOK_SUDO,    \
        DOCKER_ERROR_MESSAGE
###########################################

def get_root_dir():
    """ Get the root directory of the git repo.
    Returns:
        An absolute path.
    """
    res = command_execution_getoutput("git rev-parse --show-toplevel")
    if res[0]:
        return res[1]
    log("[git_root_dir]\n"+res[1], "error")
    sys.exit(1)

def get_git_branch():
    """ Get the current git branch.
    Returns:
        A string, the name of the branch.
    """
    res = command_execution_getoutput("git branch | grep '*' | awk '{print $2}'")
    if res[0]:
        return res[1]
    log("[get_git_branch]\n"+res[1], "error")
    sys.exit(1)

def manage_hook(git_root_dir, present=True, sudo=False):
    """ Creates or remove the hook from the .git/hook/ folder.

    Args:
        present (bool): True -> create, False -> remove
    Returns:
        A bool.
    Raises:
        FileExistsError: The file already exists, can't be created.
        FileNotFoundError: The file doesn't exists, can't delete.
    """

    # manage hook
    if present:                                             # Create the hook file
        if sudo:
            with open(git_root_dir+"/.git/hooks/pre-commit", 'w', encoding="utf-8") as file:
                file.write(PRE_COMMIT_HOOK_SUDO)
        else:
            with open(git_root_dir+"/.git/hooks/pre-commit", 'w', encoding="utf-8") as file:
                file.write(PRE_COMMIT_HOOK)

        os.chmod(git_root_dir+"/.git/hooks/pre-commit", 0o755)
        print("Git hook created.                                 \
            \nIt will execute the pipeline before the next commit.\
            \nAlternatively, you can trigger the pipeline with \'simple-ci exec\'")
    else:
        os.remove(git_root_dir+"/.git/hooks/pre-commit")   # Remove the hook file
    return True

def create_example_file(git_root_dir):
    """
    Creates an example .simple-ci.yml file at the git root dir if it doesn't exists
    """
    # check if file exists
    if os.path.isfile(git_root_dir+"/.simple-ci.yml"):
        print("File exists: Example creation skipped.")
    else:
        # create file
        with open(git_root_dir+"/.simple-ci.yml", 'w', encoding="utf-8") as file:
            file.write(EXAMPLE_FILE_DATA)
        print("The .simple-ci.yml file has been created. Check it, try it and customize it!")

def get_pipeline_data(git_root_dir, ci_script=".simple-ci.yml"):
    """ Get the pipeline data from file.
    Returns:
        A dict.
    """
    try:
        yaml_data = False
        with open(git_root_dir+"/"+ci_script, 'r', encoding="utf-8") as file:
            yaml_data = yaml.load(file, Loader=yaml.Loader)
        return yaml_data
    except FileNotFoundError:
        log("Pipeline file not found", "red")
        sys.exit(1)

def log(line, color=""):
    """ Prints line and saves it to simple.log file
    Args:
        line (str)
        color (bool)
    """
    try:
        with open("simple.log", 'a', encoding="utf-8") as log_file:
            log_file.write(line+"\n")
    except PermissionError:
        print("\033[33m"+"Warning: Can't access simple.log"+ "\033[0m")
    if color == "green":
        print("\033[32m"+line+"\033[0m")
    elif color == "red":
        print("\033[31m"+line+"\033[0m")
    elif color == "error":
        print("\033[31m"+"Error:\n"+line+"\033[0m")
    elif color == "blue":
        print("\033[36m"+line+"\033[0m")
    else:
        print(line)

def end_of_pipeline(message=""):
    """
    Display a message when pipeline failed and exits with error.
    """
    log("Error: " + message + "\nPipeline failed.", "red")
    sys.exit(1)

def command_execution_getoutput(command_to_execute):
    """
    Executes the given command
    Returns:
        (True, stdout (str)) if success
        (False, stdout (str)) if fail
    """
    res = run(command_to_execute,    \
            shell=True,              \
            stdout=PIPE,             \
            stderr=STDOUT,           \
            universal_newlines=True, \
            check=False)
    if res.returncode != 0:
        return False, res.stdout[:-1]
    return True, res.stdout[:-1]

def command_execution(command_to_execute):
    """
    Executes the given command, manage logs and exit pipeline if necessary
    """
    res = command_execution_getoutput(command_to_execute)
    log(res[1])
    if not res[0]:
        log("<<<<<<<<<<<", "red")
        log(f"Output: \n~~~~~~~~~~\n{res[1]}~~~~~~~~~~", "red")
        return False
    return True

def run_script(script_parameters):
    """Execution of the script commands on the given env."""

    script              = script_parameters[0]
    variables           = script_parameters[1]
    docker              = script_parameters[2]
    artifacts           = script_parameters[3]
    git_root_dir        = script_parameters[4]
    sudo_prefix         = script_parameters[5]
    run_name            = script_parameters[6]

    start_script_time   = time.time()

    # Prepare artifacts folder
    if artifacts:
        current_artifacts_dir   = create_artifacts_folder(git_root_dir, run_name)
        paths                   = artifacts['paths']
    else:
        current_artifacts_dir   = create_artifacts_folder("/tmp/simpleci", run_name)
        paths                   = []

    # Execution in docker
    if docker != {}:
        run_script_in_docker([          \
                script,                 \
                docker['image'],        \
                docker['path'],         \
                variables,              \
                current_artifacts_dir,  \
                sudo_prefix,            \
                paths                   \
                ])

    # Local execution
    else:
        run_script_locally([            \
                script,                 \
                git_root_dir,           \
                variables,              \
                current_artifacts_dir,  \
                sudo_prefix,            \
                paths,                  \
                ])

    return time.time() - start_script_time

def create_artifacts_folder(git_root_dir, run_name):
    """
    Creates an artifacts folder next to the git folder with same name + '-artifacts'.
    Also creates a sub-folder name after launch time.
    """
    artifacts_dir_to_be_created = git_root_dir+"-artifacts"
    try:
        os.mkdir(artifacts_dir_to_be_created)       # Create the common artifacts folder
        print("Artifacts folder created.")
    except FileExistsError:
        pass

    # list dirs in artifacts_dir_to_be_created
    run_dir = "/tmp"
    dir_list = os.listdir(artifacts_dir_to_be_created)
    run_count = 1
    while True:
        if str(run_count)+"_"+run_name in dir_list:
            run_count += 1
        else:
            run_dir = os.path.join(artifacts_dir_to_be_created,\
                    str(run_count)+"_"+run_name)
            break

    for i in (0,1,2): # If folder already exists (unlikely)
        try:
            os.mkdir(run_dir)             # Create the run folder
            break
        except FileExistsError:
            print(f"Run folder already exists. (try: {i+1})")
            time.sleep(1.5)
            run_dir = os.path.join(artifacts_dir_to_be_created,\
                datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            if i < 2:
                continue
            end_of_pipeline()
    return run_dir

def run_script_locally(script_parameters):
    """
    Local cript execution.
    """
    script                  = script_parameters[0]
    git_root_dir            = script_parameters[1]
    variables               = script_parameters[2]
    current_artifacts_dir   = script_parameters[3]
    sudo_prefix             = script_parameters[4]
    paths                   = script_parameters[5]
    tmp_artifacts_dir       = "/tmp/" \
                            + os.path.basename(current_artifacts_dir)

    if git_root_dir != tmp_artifacts_dir:           # For nested simpleci exec
        command = f"{sudo_prefix} bash -c \
                  \'cp -r {git_root_dir} {tmp_artifacts_dir}\'"
        res = command_execution_getoutput(command)
        if not res[0]:
            end_of_pipeline("[run_script:shell]\n"+res[1])

    current_dir = os.getcwd()                       # Save working dir
    os.chdir(tmp_artifacts_dir)
    for command in script:
        log("## > " + str(command), "green")
        if not exec_script_command(     \
                command,                \
                variables,              \
                sudo_prefix=sudo_prefix):
            end_of_pipeline(f"Command \'{command}\' execution failed.")

    # Artifacts
    for file in paths:
        res = command_execution_getoutput(f"{sudo_prefix} cp -r -t \
                {current_artifacts_dir} {tmp_artifacts_dir}/{file} ")
        if not res[0]:
            end_of_pipeline(                                    \
                    f"Artifact \'{file}\' couldn't be found.\n  \
                    -> Check the pipeline syntax."              \
                    )
        log(f"Artifact \"{file}\" saved in {current_artifacts_dir}.", "blue")

    os.chdir(current_dir)                           # Back to working dir

def exec_script_command(script_command, env, sudo_prefix=""):
    """  Execute a command with a given env
    Args:
        command (str)
        env (dict)
    """
    env_cmd = "true"

    for var_key in env:                                         # Add env variables declaration
        env_cmd = env_cmd + \
                " && " +    \
                var_key + "=\"" + str(env[var_key]) + "\""

    passed_command = sudo_prefix +  \
            "bash -c \'" +          \
            env_cmd +               \
            " && " +                \
            script_command +        \
            "\'"                                                # Assemble final command
    return command_execution(passed_command)

def run_script_in_docker(script_parameters):
    """
    Script execution in docker.
    """
    script                  = script_parameters[0]
    docker_image            = script_parameters[1]
    docker_path             = script_parameters[2]
    variables               = script_parameters[3]
    current_artifacts_dir   = script_parameters[4]
    sudo_prefix             = script_parameters[5]
    paths                   = script_parameters[6]

    log(f"A \'{docker_image}\' container is required.", "blue")

    docker_ok = command_execution(sudo_prefix+"docker ps > /dev/null")
    if not docker_ok:                   # Check if script can access docker
        end_of_pipeline(DOCKER_ERROR_MESSAGE)

    container_id = create_container(    \
            docker_image,               \
            sudo_prefix=sudo_prefix     \
            )                           # Creating container
    log(f"Container \'{container_id}\' as been created.", "blue")

    copy_files_to_docker(               \
            container_id,               \
            docker_path,                \
            sudo_prefix=sudo_prefix     \
            )                           # copy files to docker

    for command in script:              # Exec script in docker
        log("## > " + str(command), "green")
        if not exec_script_command_in_docker(   \
                command,                        \
                variables,                      \
                container_id,                   \
                sudo_prefix=sudo_prefix):
            stop_container(                     \
                container_id,                   \
                sudo_prefix=sudo_prefix         \
                )                       # Kill container
            end_of_pipeline(f"Command \'{command}\' execution failed in docker.")

    # Artifacts
    for file in paths:
        res = command_execution_getoutput\
                (f"{sudo_prefix} docker cp {container_id}:{file} {current_artifacts_dir}")
        if not res[0]:
            end_of_pipeline(                                    \
                    f"Artifact \'{file}\' couldn't be found.\n  \
                    -> Check the pipeline syntax."              \
                    )
        log(f"Artifact \"{file}\" saved in {current_artifacts_dir}.", "blue")

    stop_container(                 \
            container_id,           \
            sudo_prefix=sudo_prefix \
            )                           # Kill container

def create_container(docker_image, sudo_prefix=""):
    """
    Creates a docker container of the specified image.
    Returns:
        container_hash (str)
    """
    res = command_execution_getoutput(sudo_prefix+"docker run -td " + docker_image)
    if res[0]:
        container_hash = res[1].split(sep='\n')[-1][0:11]
        return container_hash
    log("[create_container]\n"+res[1], "error")
    sys.exit(1)

def copy_files_to_docker(cont_id, path, sudo_prefix=""):
    """
    Copies the current git folder to container at the given path.
    """
    log(f"Files will be copied to the container {cont_id} at \'{path}\'", "blue")
    res = command_execution_getoutput(f"{sudo_prefix} docker cp . {cont_id}:{path}")
    if not res[0]:
        log("[copy_files_to_docker]\n"+res[1], "error")
        end_of_pipeline()

def exec_script_command_in_docker(script_command, env, cont_id, sudo_prefix=""):
    """
    Execute a command with the given env in the given container.
    """
    env_cmd = "true"

    for var_key in env:                                         # Add env variables declaration
        env_cmd = env_cmd + \
                " && " +    \
                var_key + "=\"" + str(env[var_key]) + "\""

    passed_command = "sh -c \'" + \
            env_cmd +             \
            " && " +              \
            script_command +      \
            "\'"                                                # Assemble final command
    full_command = sudo_prefix + "docker exec " + cont_id + " " + passed_command+ " \n"
    return command_execution(full_command)

def stop_container(cont_id, sudo_prefix=""):
    """
    Stops a docker container.
    """
    res = command_execution_getoutput(sudo_prefix + "docker rm -f " + cont_id + " > /dev/null")
    if not res[0]:
        log("[stop_container]\n"+res[1], "error")
        end_of_pipeline()
