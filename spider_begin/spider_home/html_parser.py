# -*- coding: utf-8 -*-

# 页面解析模块：产生新的URL链接，获取词条名称和信息

import re
import urlparse
import urllib2



class HtmlParser(object):

    def parse(self, page_url, html_cont,soup):
        if page_url is None or html_cont is None:
            return

       
        new_urls = self._get_new_urls(page_url, soup)
 
#         new_data = self._get_new_data(page_url, soup)
        return new_urls
#     , new_data
    

    def _get_new_urls(self, page_url, soup):
        url = 'http://www.dailywell.com.tw/'
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/s/"))
        for link in links:
            new_url = link['href']
#             reChinese = re.compile('[\x80-\xff]+')
#             word = reChinese.findall(new_url)
#             if word=='展覽資訊':
#                 rep = urllib2.quote('展覽資訊')
#                 new_url=link.replace('展覽資訊', rep)
#             new_url=new_url.encode('utf-8')
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls
#     def get_pdf(self,catch,html_content,soup):
#         url = 'http://www.dailywell.com.tw/'
# #     catch='http://www.dailywell.com.tw/s/2/product-465210/Miniature-Toggle-Switches-1M-Series.html'
# 
# 
#         html = requests.get(catch).text
# #         soup = BeautifulSoup(html,'html.parser')
# 
#         pdf_url=re.findall('<a\s*href\s*="?(\S+).pdf"',html,re.S)
#         name=soup.find('h1',class_="name").get_text()
#         if name.find(' '):
#             name=re.sub(' ','',name)
#             name=re.sub('\r\n','',name)
#             print name
#         for each in pdf_url:
#    
#     
#             judge=each.find("../../../c")
#             if judge!=-1:
#                 each=each.replace("../../../",url)+".pdf"
#                 print each
#             pdf=requests.get(each,timeout=10)
# 
#             string = 'pdf\\'+name+'.pdf'
#             fp = open(string,'wb')
#             fp.write(pdf.content)
#             fp.close()
#     def _get_new_data(self, page_url, soup):
#         res_data = {}
# 
#         # url
#         res_data['url'] = page_url
#         
#         # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
#         title_node = soup.find('dd', class_= "lemmaWgt-lemmaTitle-title").find("h1")
#         res_data['title'] = title_node.get_text()
# 
#         # <div class="lemma-summary" label-module="lemmaSummary">
#         summary_node = soup.find('div', class_="lemma-summary")
#         res_data['summary'] = summary_node.get_text()
#         
#         return res_data
