import os
import os.path

def scanfiles(directory_path):
    directory_path = os.path.expanduser(directory_path)
    files_and_dirs = os.listdir(directory_path)
    # Filter out directories, keeping only files
    files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory_path, f))]
    return files


