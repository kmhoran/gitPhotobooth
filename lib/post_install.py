import os
import sys
import lib



dist_file = os.path.dirname(lib.__file__)


def get_git_directory(folder):
    if '.git' in os.listdir(folder):
        return os.path.join(folder, '.git')
    elif folder == '/':
        return None
    else:
        return get_git_directory(os.path.dirname(folder))


def is_photobooth_file(path):
    "determine if file belongs to photobooth"
    with open(path, 'rb') as file:
        if b"PHOTOBOOTH FILE" in file.read():
            return True
    return False


def install_photobooth(git_directory):
    destination_folder = os.path.join(git_directory, 'hooks', 'photobooth')
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    # Remove existing photobooth files to ensure a clean install
    for file_name in os.listdir(destination_folder):
        existing = os.path.join(destination_folder, file_name)
        if os.path.isfile(existing) and is_photobooth_file(existing):
            os.remove(existing)

    source_folder = os.path.join(dist_file, 'photobooth')

    for file_name in os.listdir(source_folder):
        if not file_name.endswith('.py'):
            continue
        source = os.path.join(source_folder, file_name)
        destination = os.path.join(destination_folder, file_name)

        if os.path.exists(destination) and not is_photobooth_file(destination):
            print("'{0}' already exists. Not installing.".format(file_name))
            continue
        print("Installing photobooth file: '{0}'.".format(file_name))
        os.system("cp {0} {1}".format(source, destination))


def install_git_hooks(git_directory):
    print("Installing post_commit.py to '{0}'.".format(git_directory))
    post_commit_source = os.path.join(dist_file, 'post_commit.py')
    post_commit_destination = os.path.join(git_directory, 'hooks', 'post-commit')
    if os.path.exists(post_commit_destination):
        if is_photobooth_file(post_commit_destination):
            print("Overwriting existing photobooth file at {0}".format(post_commit_destination))
        else:
            print("A file already exists at ''. Please reamove it and try again".format(post_commit_destination))
            sys.exit(1)
    os.system("cp {0} {1}".format(post_commit_source, post_commit_destination))
    os.system("chmod +x {0}".format(post_commit_destination))


def make_git_hooks(git_directory):
    hooks_folder = os.path.join(git_directory, 'hooks')
    if not os.path.exists(hooks_folder):
        os.mkdir(hooks_folder)
    install_git_hooks(git_directory)


def run_post_install():
    if sys.version_info < (3, 5):
        print("Your version of python is too old. gitPhotoBooth requires 3.5 and above.")
        sys.exit(1)

    git_directory = get_git_directory(os.getcwd())
    if not git_directory:
        print("This project must be installed in an active git project. Please try again.")
        sys.exit(1)

    print("Installing photobooth.")
    make_git_hooks(git_directory)
    install_photobooth(git_directory)