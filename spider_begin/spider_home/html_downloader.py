# -*- coding: utf-8 -*-
#页面下载模块

import urllib2

import requests
# def check_ch(check_str):
#             for ch in check_str.decode('utf-8'):
#                 if u'\u4e00' <= ch <= u'\u9fff':
#                     return True
#                 return False
#             rep = urllib2.quote('展覽資訊')
#             url=url.replace('展覽資訊', name)
class HtmlDownloader(object):
    

    def download(self, url):
        name = urllib2.quote("展覽資訊") 
#         url = urllib2.quote(url)
#         url=url.replace('%3A',':')
        if url.find(name):
            response=requests.get(url)
            return response.text
        
        else:
            if url is None:
                return None
            response = urllib2.urlopen(url)
            if response.getcode() != 200:
                return None
        return response.read()
        