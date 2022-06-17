import os


def find_files():
    # number of files
    count = 0
    # find directories and files in data directory
    for ds_and_fs in os.walk('data'):
        index = 0
        for path in ds_and_fs:
            if index == 0:
                print("directory:", path)
            else:
                for sub_path in path:
                    print(count, sub_path)
                    count += 1
            index += 1


def data_parser():
    print("files in data directory: ")
    find_files()


# function to test parser
def init_main():
    data_parser()


# run to test parser
init_main()
