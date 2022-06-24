import matplotlib.pyplot as plt
import data_loader as dp


def plot(variables, df):
    plt.plot(df[variables[0]], df[variables[1]], 'bo')
    plt.show()


def plotter(df):
    columns = list(df.columns)
    index = 0
    print("--------- variables ---------")
    for column in columns:
        print(index, column)
        index += 1
    print("select variables (0,1 - x,y)")
    variablesString = input()
    variablesIndices = variablesString.split(',')
    variables = []
    for index in variablesIndices:
        if int(index) < len(columns):
            variables.append(columns[int(index)])
    plot(variables, df)


def main():
    df = dp.data_loader()
    plotter(df)


if __name__ == "__main__":
    main()
