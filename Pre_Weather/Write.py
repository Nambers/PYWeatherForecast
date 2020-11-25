import re

from GetData import GetData
from bs4 import *
import datetime as DT
import csv


# 功能: 写csv

def Write(years, b, c):
    # 1. 创建文件对象
    f = open(c, 'w', encoding='utf-8', newline='')

    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)

    # 3. 构建列表头
    csv_writer.writerow(["Time", "Ave_t", "Max_t", "Min_t", "Prec", "SLpress", "Winddir", "Windsp", "Cloud"])
    for a in years:
        # 取现在日期
        today = DT.datetime.now()
        # 取7天前日期
        week_ago = (today - DT.timedelta(days=b[0])).date()
        # 七天后
        week_pre = (today + DT.timedelta(days=b[1])).date()
        # 爬取数据链接
        url = "http://www.meteomanz.com/sy2?l=1&cou=2250&ind=59287&d1=" + str(week_ago.day).zfill(2) + "&m1=" + str(
            week_ago.month).zfill(2) + "&y1=" + str(today.year - a) + "&d2=" + str(week_pre.day).zfill(
            2) + "&m2=" + str(
            week_pre.month).zfill(2) + "&y2=" + str(today.year - a)
        g = GetData(url).Get()
        # beautifulsoup解析网页
        soup = BeautifulSoup(g, "html5lib")
        # 取<tbody>内容
        tb = soup.find(name="tbody")
        # 取tr内容
        past_tr = tb.find_all(name="tr")
        for tr in past_tr:
            # 取tr内每个td的内容
            text = tr.find_all(name="td")
            flag = False
            for i in range(0, len(text)):
                if i == 0:
                    text[i] = text[i].a.string
                    # 网站bug，会给每个月第0天，比如 00/11/2020,所以要drop掉
                    if "00/" in text[i]:
                        flag = True
                elif i == 8:
                    # 把/8去掉，网页显示的格式
                    text[i] = text[i].string.replace("/8", "")
                elif i == 5:
                    # 去掉单位
                    text[i] = text[i].string.replace(" Hpa", "")
                elif i == 6:
                    # 去掉风力里括号内的内容
                    text[i] = re.sub(u"[º(.*?|N|W|E|S)]", "", text[i].string)
                else:
                    # 取每个元素的内容
                    text[i] = text[i].string
                # 丢失数据都取2(简陋做法)
                # 这么做 MAE=3.6021
                text[i] = text[i].replace("-", "2")
                text[i] = text[i].replace("Tr", "2")
            # 4. 写入csv文件内容
            if not flag:
                csv_writer.writerow(text)
    # 5. 关闭文件
    f.close()
