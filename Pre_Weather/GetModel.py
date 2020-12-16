# -*- coding: utf-8 -*-
# @Time: 2020/12/16
# @Author: Eritque arcus
# @File: GetModel.py
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.metrics import mean_absolute_error
from ProcessData import ProcessData


# 训练并保存模型
def GetModel(a="Model.pkl"):
    """
    :param a: 模型文件名
    :return:
        [socre: MAE评估结果,
        X_test: 预测数据集]
    """
    # 取到数据
    [X_train, X_valid, y_train, y_valid, X_test] = ProcessData()
    # 用XGB模型，不过用有bug
    # modelX = XGBRegressor(n_estimators=1000, learning_rate=0.05, random_state=0, n_jobs=4)
    # # model.fit(X_train_3, y_train_3)
    # # model.fit(X_train_2, y_train_2)
    # col = ["Ave_t", "Max_t", "Min_t", "Prec","SLpress", "Winddir", "Windsp", "Cloud"]
    # modelX.fit(X_train, y_train,
    #           early_stopping_rounds=5,
    #           eval_set=[(X_valid, y_valid)],
    #           verbose=False)
    # 随机树森林模型
    model = RandomForestRegressor(random_state=0, n_estimators=1001)
    # 训练模型
    model.fit(X_train, y_train)
    # 预测模型，用上个星期的数据
    preds = model.predict(X_valid)
    # 用MAE评估
    score = mean_absolute_error(y_valid, preds)
    # 保存模型到本地
    joblib.dump(model, a)
    # 返回MAE
    return [score, X_test]
