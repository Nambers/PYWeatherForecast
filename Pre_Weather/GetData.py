# -*- coding: utf-8 -*-
# @Time: 2020/12/16
# @Author: Eritque arcus
# @File: GetData.py
# 功能: 爬取数据
import urllib3


class GetData:
    url = ""
    headers = ""

    def __init__(self, url, header=""):
        """
        :param url: 获取的网址
        :param header: 请求头，默认已内置
        """
        self.url = url
        if header == "":
            self.headers = {
                'Connection': 'Keep-Alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                              'like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36 ',
                'Host': 'www.meteomanz.com'
            }
        else:
            self.headers = header

    def Get(self):
        """
        :return: 网址对应的网页内容
        """
        http = urllib3.PoolManager()
        return http.request('GET', self.url, headers=self.headers).data
