import matplotlib.pyplot as plt


def plot(variables, df):
    plt.plot(df[variables[0]], df[variables[1]], 'bo')
    plt.show()


def plotter(df):
    columns = list(df.columns)
    df_binary = df[columns]
    index = 0
    print("----- Variables -----")
    for column in columns:
        print(index, column)
        index += 1
    print("select variables (0,1 - x,y")
    variablesString = input()
    variablesIndices = variablesString.split(',')
    variables = []
    for index in variablesIndices:
        if int(index) < len(columns):
            variables.append(columns[int(index)])
    plot(variables, df)
