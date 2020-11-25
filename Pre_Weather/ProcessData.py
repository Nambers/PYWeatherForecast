from sklearn import preprocessing
from Write import Write
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
# 功能: 数据预处理

def ProcessData():
    # 用近几年的数据做训练集
    # 如 years = [2,1]就是用2019和2018年现在的(这个时候)数据做训练集
    years = [1]
    # 写入csv
    Write(years, [7, 0], "weather_train_train.csv")
    Write(years, [0, 7], "weather_train_valid.csv")
    Write([0], [7, 0], "weather_test.csv")

    # 读取测试集和验证集
    X = pd.read_csv("weather_train_train.csv", index_col="Time", parse_dates=True)
    y = pd.read_csv("weather_train_valid.csv", index_col="Time", parse_dates=True)
    X_test = pd.read_csv("weather_test.csv", index_col="Time", parse_dates=True)

    # 数据归一化
    # scaler = preprocessing.StandardScaler()
    # pars = [cols for cols in X.columns if cols != "Time"]
    # for data in [X, y, X_test]:
    #     for par in pars:
    #         data[par] = scaler.fit_transform(data[par].values.reshape(-1, 1))
    #         # temp = scaler.fit(data[par].values.reshape(-1, 1))
    #         # data[par] = scaler.fit_transform(data[par].values.reshape(-1, 1), temp)

    # # 画折线图
    # sns.lineplot(data=X)
    # plt.show()
    # sns.lineplot(data=y)
    # plt.show()
    # sns.lineplot(data=X_test)
    # plt.show()
    # 返回分割后的数据集
    return [train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0), X_test]
