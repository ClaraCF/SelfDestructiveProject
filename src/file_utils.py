import os


def Read(filename: str) -> bytes:
    with open(filename, "rb") as file:
        backup = file.read()
    return backup


def Write(filename: str, data: bytes):
    with open(filename, "wb+") as file:
        file.write(data)


# This function recursively saves all files in the project directory to memory
def Backup(directory: str) -> dict:   # Returns a dictionary with all files and its data in bytes
    project = dict()

    # Save current directory and enter specified dir
    initial_dir = os.getcwd()
    os.chdir(directory)

    for file in os.listdir(directory):
        file = os.path.abspath(file)

        if os.path.isdir(file):
            project.update({file: Backup(file)})

        else:
            project.update({file: Read(file)})

    # Return to the initial directory
    os.chdir(initial_dir)

    return project


# This functions returns all files  in  memory back to disk
def Restore(project: dict):
    for file in project:

        # If the value is another dict, it means it used to be a dir...
        if isinstance(project[file], dict):
            os.mkdir(file)          # ...so create it first
            Restore(project[file])

        else:
            Write(file, project[file])
