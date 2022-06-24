import os
import csv
import pandas as pd


def find_files():
    # number of files
    count = 0
    # files path list
    files = []
    # find directories and files in data directory
    for ds_and_fs in os.walk('data'):
        index = 0
        dir = ""
        for path in ds_and_fs:
            if index == 0:
                print("directory:", path)
                dir = path
            else:
                for sub_path in path:
                    length = len(sub_path)
                    if sub_path[length-3:length:1] == 'csv':
                        filepath = dir + "/" + sub_path
                        files.append(filepath)
                        print(count, sub_path)
                        count += 1
            index += 1
    return files


def clean_csv(path):
    with open(path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line == 0:
                print(row)
                line += 1


def data_loader():
    print("--------- load file ---------")
    # find files
    print("files in data directory: ")
    files = find_files()
    # select file
    print("select file: ")
    selection = int(input())
    # parse csv
    df = pd.read_csv(files[selection])
    return df


'''
# function to test parser
def __main():
    data_parser()

# run to test parser
main()
'''