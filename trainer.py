import data_loader as dp
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics


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


def multiple_linear_regression(var_names, df):
    print("------------------------- multiple linear regression -------------------------")
    print("enter test size: ")
    test_size = int(input())
    # create x matrix from df
    x = df[var_names[0:len(var_names)-1]]
    # create y matrix from df
    y = df[var_names[len(var_names)-1:len(var_names)]]

    # splitting x and y into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=1)

    # create linear regression object
    reg = linear_model.LinearRegression()

    # train the model using the training sets
    reg.fit(x_train, y_train)

    # regression coefficients
    print('coefficients: ', reg.coef_)

    # variance score: 1 means perfect prediction
    print('variance score: {}'.format(reg.score(x_test, y_test)))

    # plot for residual error

    # setting plot style
    plt.style.use('fivethirtyeight')

    # plotting residual errors in training data
    plt.scatter(reg.predict(x_train), reg.predict(x_train) - y_train, color="green", s=10, label='train data')

    # plotting residual errors in test data
    plt.scatter(reg.predict(x_test), reg.predict(x_test) - y_test, color="blue", s=10, label='test data')

    # plotting line for zero residual error
    plt.hlines(y=0, xmin=0, xmax=50, linewidth=2)

    # plot legend
    plt.legend(loc = 'upper right')

    # plot title
    plt.title('residual errors')

    # show plot
    plt.show()


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
        multiple_linear_regression(variables, df)
    print("------------------------------------------------------------------------------")
    print("//////////////////////////////////////////////////////////////////////////////")


def main():
    df = dp.data_loader()
    trainer(df)


if __name__ == "__main__":
    main()
