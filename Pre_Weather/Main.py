import joblib
import datetime as DT
from GetModel import GetModel

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
for a in range(1, 7):
    today = DT.datetime.now()
    time = (today + DT.timedelta(days=a)).date()
    print(time.year, '/', time.month, '/', time.day, ': 平均气温', preds[a][0], '最高气温', preds[a][1],
          '最低气温', preds[a][2], "降雨量", preds[a][3], "风力", preds[a][4])
