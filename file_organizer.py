import os


# os.walk through a directory and return a list of file contents
def get_file_list(input):

    file_list = []
    try:
        for root, dirs, files in os.walk(input):
            for name in files:
                file_list.append(os.path.join(root, name))
    except Exception:
        pass
    return file_list


# returns string of new numbered path in case of duplicate file names
def generate_numbered_path(path, number):

    number = ' (' + str(number) + ')'
    root, file = os.path.split(path)
    file, ext = os.path.splitext(file)
    new_file = file + number + ext
    new_path = os.path.join(root, new_file)
    return new_path


# creates new directory if it does not exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def sort_file_list(file_list, output):

    for path in file_list:
        try:
            # separate root, file and extension
            root, file = os.path.split(path)
            file, ext = os.path.splitext(file)
            output_directory = os.path.join(output, ext[1:])

            create_directory(output_directory)

            new_file = os.path.join(output_directory, file + ext)

            if os.path.exists(new_file):
                number = 2
                new_file_numbered = generate_numbered_path(new_file, number)
                while os.path.exists(new_file_numbered):
                    number += 1
                    new_file_numbered = generate_numbered_path(new_file, number)

                os.rename(path, new_file_numbered)
                continue
            else:
                os.rename(path, new_file)

        except Exception:
            print("errors")


def organize(input, output):

    for root in input:
        file_list = get_file_list(root)
        sort_file_list(file_list, output)
