# PYWeatherReport
## 简介
一个用python机器学习(ml)做的广州地区的简易天气预报

模型是用的决策树森林

在Pre_Weather文件夹下用 python Main.py 命令运行

训练数据来源于[http://www.meteomanz.com/](http://www.meteomanz.com/)

## 如何使用

直接用python运行`pre_weather/Main.py`，就会在控制台输出预测的数据
```
python pre_weather/Main.py
```
或

在你的python代码里用`joblib`导入生成的模型，然后输入你的数据进行预测

(PS: 因为模型的训练用的数据日期和你预测数据的日期有关，所以不建议直接用使用非当天训练的模型进行预测，误差可能偏大)

如以下代码(在Main.py的11行):
```
import joblib

# 读取保存的模型
model = joblib.load('Model.pkl')

# 最终预测结果
preds = model.predict(r[1])
```
其中，`r[1]`是预测数据

或

参考`Main.py`，自己写一个符合你需求启动文件
## 系列教程

[机器学习参考篇: python+sklearn+kaggle机器学习](https://blog.csdn.net/qq_40832960/article/details/109260388)

[用python+sklearn(机器学习)实现天气预报 准备](https://blog.csdn.net/qq_40832960/article/details/111146467)

[用python+sklearn(机器学习)实现天气预报数据 数据](https://blog.csdn.net/qq_40832960/article/details/111182425)

 [用python+sklearn(机器学习)实现天气预报 模型和使用](https://blog.csdn.net/qq_40832960/article/details/111238926)
 
> 2020/12/16

优化和修复代码，增加数据可视化显示
![CSDNimage](https://img-blog.csdnimg.cn/20201216163833585.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODMyOTYw,size_16,color_FFFFFF,t_70)

> 2020/12/7

优化和修复代码

增加模型保存和填充缺失数据

> 2020/11/25

优化了代码

计划未来改模型为RGBoost或用tensorflow来降低MAE，同时提高数据多元化

MAE优化到3.6021665834173815

把丢失值取为手动平均值2

![image](https://s3.ax1x.com/2020/11/25/DdngHO.png)

> 2020/11/24

模型是用的决策树森林

训练数据来源于[http://www.meteomanz.com/](http://www.meteomanz.com/)

MAE目前是3.604，未来我会尽可能继续优化

![image](https://github.com/Nambers/PYWeatherReport/blob/main/result.jpg)

