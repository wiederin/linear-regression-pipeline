import data_loader as dp
import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
    # number of observations
    n = np.size(x)

    # mean of x and y vectors
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculate cross-deviation and deviation about x
    ss_xy = np.sum(y*x) - n * m_y * m_x
    ss_xx = np.sum(x*x) - n * m_x * m_x

    # calculate regression coefficients
    b_1 = ss_xy / ss_xx
    b_0 = m_y - b_1 * m_x

    return b_0, b_1


def plot_regression_line(xName, yName, x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m", marker="o", s= 30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # add labels
    plt.xlabel(xName)
    plt.ylabel(yName)

    # show plot
    plt.show()


def simple_linear_regression(xName, yName, x, y):
    print("-------------------------- simple linear regression --------------------------")
    b = estimate_coef(x, y)
    print("estimated coefficients: \nb_0 = {} \nb_1 = {}".format(b[0], b[1]))
    plot_regression_line(xName, yName, x, y, b)


#def multiple_linear_regression(var_names):



def trainer(df):
    columns = list(df.columns)
    index = 0
    print("--------------------------------- variables ----------------------------------")
    for column in columns:
        print(index, column)
        index += 1
    print("select variables (0,1 - x,y or 0,1,2 x1, x2, y)")
    variablesString = input()
    variablesIndices = variablesString.split(',')
    variables = []
    for index in variablesIndices:
        if int(index) < len(columns):
            variables.append(columns[int(index)])
    # simple linear regression
    if len(variables) < 2:
        print("error only one variable selected")
    elif len(variables) == 2:
        simple_linear_regression(variables[0], variables[1], df[variables[0]], df[variables[1]])
    else:
        #multiple_linear_regression(variables)
        print(df)

def main():
    df = dp.data_loader()
    trainer(df)


if __name__ == "__main__":
    main()
