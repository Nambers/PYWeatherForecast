from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
from ProcessData import ProcessData
from sklearn.ensemble import RandomForestRegressor
import datetime as DT
import pandas as pd
from xgboost import XGBRegressor

# 取到数据
[[X_train, X_valid, y_train, y_valid],  X_test] = ProcessData()
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
model = RandomForestRegressor(random_state=0, n_estimators=1000)
# 训练模型
model.fit(X_train, y_train)
# 预测模型，用上个星期的数据
preds = model.predict(X_valid)
# 用MAE评估
score = mean_absolute_error(y_valid, preds)
print('MAE:', score)
# 最终预测结果
preds = model.predict(X_test)
# 反归一化，不过出bug了
# for cols in range(0, len(preds)):
#     preds[cols] = scaler.inverse_transform(preds[cols])
# sns.lineplot(data=preds)
# plt.show()
# 打印结果到控制台
print("未来7天预测")
for a in range(1, 7):
    today = DT.datetime.now()
    time = (today + DT.timedelta(days=a)).date()
    print(time.year, '/', time.month, '/', time.day, ': 平均气温', preds[a][0], '最高气温', preds[a][1],
          '最低气温', preds[a][2], "降雨量", preds[a][3], "风力", preds[a][4])
