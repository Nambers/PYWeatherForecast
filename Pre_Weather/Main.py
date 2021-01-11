# -*- coding: utf-8 -*-
# @Time: 2020/12/16
# @Author: Eritque arcus
# @File: Main.py
import joblib
import datetime as DT
from GetModel import GetModel
import matplotlib.pyplot as plt


def findNeg(t, n: int):
    return n if t == 0 else -n


# 训练并保存模型并返回MAE
r = GetModel()
print("MAE:", r[0])
# 读取保存的模型
model = joblib.load('Model.pkl')

# 最终预测结果
preds = model.predict(r[1])
# 反归一化或标准化，不过出bug了，不用
# for cols in range(0, len(preds)):
#     preds[cols] = scaler.inverse_transform(preds[cols])
# sns.lineplot(data=preds)
# plt.show()
# 打印结果到控制台
print("未来7天预测")
print(preds)
all_ave_t = []
all_high_t = []
all_low_t = []
for a in range(1, 7):
    today = DT.datetime.now()
    time = (today + DT.timedelta(days=a)).date()
    print(time.year, '/', time.month, '/', time.day,
          ': 平均气温',  preds[a][0],
          '最高气温', preds[a][1],
          '最低气温', preds[a][2],
          "降雨量", preds[a][3],
          "风力", preds[a][4])
    all_ave_t.append(preds[a][0])
    all_high_t.append(preds[a][1])
    all_low_t.append(preds[a][2])
temp = {"ave_t": all_ave_t, "high_t": all_high_t, "low_t": all_low_t}
# 绘画折线图
plt.plot(range(1, 7), temp["ave_t"], color="green", label="ave_t")
plt.plot(range(1, 7), temp["high_t"], color="red", label="high_t")
plt.plot(range(1, 7), temp["low_t"], color="blue", label="low_t")
plt.legend()  # 显示图例
plt.ylabel("Temperature(°C)")
plt.xlabel("day")
# 显示
plt.show()
