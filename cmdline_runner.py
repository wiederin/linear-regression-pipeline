import data_loader as dp
import plotter as plt
import trainer as trn


def main():
    df = dp.data_loader()
    while True:
        print("---------- options ----------")
        print("0 plot")
        print("1 train")
        print("x exit")
        selection = input()
        if selection is '0':
            print("---------- plotter ----------")
            plt.plotter(df)
        elif selection is '1':
            trn.trainer(df)
        elif selection is 'x':
            break


if __name__ == "__main__":
    main()
