import data_parser as dp
import plotter as plt


def main():
    df = dp.data_parser()
    print("-------- Options --------")
    print("0 plot")
    selection = 0
    if selection is 0:
        plt.plotter(df)


main()
