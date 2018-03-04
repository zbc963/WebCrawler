# -*- coding: utf-8 -*-


# 爬虫调度端

import url_manager, html_downloader, html_parser,pdf_download,download
from bs4 import BeautifulSoup

class SpiderMain(object):
    
    # 初始化url_manager、html_downloader、html_parser、html_outputer四个模块
    def __init__(self):
        self.maxcount = 1000    #设置最大抓取数据数量
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.pdf = pdf_download.PdfDownload()
        self.pic = download.PicDowload()
#         self.outputer = html_outputer.HtmlOutputer()
    
    # 执行爬虫，爬取1000个root_url下相关的链接，并输出到out_put.html
    def craw(self, root_url):
        
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
#             try :
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                
                html_cont = self.downloader.download(new_url)
                soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
                new_urls = self.parser.parse(new_url, html_cont,soup)
# .new_data     

#                 self.pdf.get_pdf(new_url,soup,html_cont)
                self.pic.get_pics(new_url,soup,html_cont)
                self.urls.add_new_urls(new_urls)
                
#                 self.outputer.collect_data(new_data)

                if count == self.maxcount:
                    break
                count = count + 1
#             except:
#                 print 'craw failed'

#         self.outputer.output_html()

if __name__ == "__main__":

    root_url = 'http://www.dailywell.com.tw/?lang=2&TTo=en'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
