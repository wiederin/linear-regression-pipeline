import data_parser as dp
import plotter as plt


def main():
    df = dp.data_parser()
    while True:
        print("---------- Options ----------")
        print("0 plot")
        print("1 train")
        print("x exit")
        selection = input()
        if selection is '0':
            plt.plotter(df)
        elif selection is '1':
            print("train")
        elif selection is 'x':
            break


main()
