import os

error_log = []


def get_file_list(input):

    file_list = []
    try:
        for root, dirs, files in os.walk(input):
            for name in files:
                file_list.append(os.path.join(root, name))
    except Exception:
        pass
    return file_list


def generate_new_path(path, number):

    number = ' (' + str(number) + ')'
    root, file = os.path.split(path)
    file, ext = os.path.splitext(file)
    new_file = file + number + ext
    new_path = os.path.join(root, new_file)
    return new_path


def sort_file_list(file_list, output):

    for path in file_list:
        try:
            root, file = os.path.split(path)
            file, ext = os.path.splitext(file)

            output_directory = os.path.join(output, ext[1:])

            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            new_file = os.path.join(output_directory, file + ext)

            if os.path.exists(new_file):
                number = 2
                new_file_numbered = generate_new_path(new_file, number)

                while os.path.exists(new_file_numbered):
                    number += 1
                    new_file_numbered = generate_new_path(new_file, number)

                os.rename(path, new_file_numbered)
                continue

            else:
                os.rename(path, new_file)

        except Exception:
            print("errors")


def main():
    input = 'D:\Libraries\Documents\Programming\Projects\python-organizer\\test_files\input'
    output = 'D:\Libraries\Documents\Programming\Projects\python-organizer\\test_files\output'

    file_list = get_file_list(input)
    sort_file_list(file_list, output)


if __name__ == '__main__':
    main()