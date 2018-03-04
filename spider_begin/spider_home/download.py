# -*- coding: utf-8 -*-
'''
Created on May 9, 2017

@author: Jzzz
'''


import re
import requests
from bs4 import BeautifulSoup
import os


 
           
            
class PicDowload(object):
    def get_pics(self,catch,soup,html):
        url = 'http://www.dailywell.com.tw/'
#     catch='http://www.dailywell.com.tw/s/2/product-c105837/Toggle-Switches.html'
#         html = requests.get(catch).text
#         soup=BeautifulSoup(html,'html.parser',from_encoding="utf-8")
        if soup.find('h2',class_="item"):
            name=soup.find('h2',class_="item").get_text()
            if name.find('/'):
                name=re.sub('/','',name)
        else:
            name='else'
        name=re.sub('\s','',name)
        print name
#print html

        pic_url = re.findall('<img\s*src\s*="?(\S+)"?',html,re.S)
# new_url = re.findall('<a\s*href\s*="?(\S+)"?',html,re.S)
        i = 0
# for each in new_url:
#     print each 
        for each in pic_url:
            check1=".jpg"
            check2=".png"
            judge1= each.find(check1)
            judge2=each.find(check2)
            if judge1 != -1:
                ind=each.index(check1)+4
                ind=ind-len(each)
                each=each[:ind]
#                 print each+"\n"
            if judge2 != -1:
                ind=each.index(check2)+4
                ind=ind-len(each)
                each=each[:ind]
#                 print each+"\n"
            try:
                error1="../../../c"
                error2="../../c"
  
                jud1=each.find(error1)
                jud2=each.find(error2)
         
                if jud1!=-1:
                    each=each.replace(error1,url+"c")
        
                elif jud2!=-1:
                    each=each.replace(error2,url+"style/c")
                else:
                    each=url+each
                print each
         
            except requests.exceptions.ConnectionError:
                print '(error) unable download'
                continue
            pic= requests.get(each, timeout=10)
            newpath = r'F:\cmpt276 andriod\eclipse workspace\spider_begin\spider_home\DailywellSwitchPic/'+name
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            string = 'DailywellSwitchPic/'+name+'\\'+name+str(i) + '.jpg'
            fp = open(string,'wb')
            fp.write(pic.content)
            fp.close()
            i += 1
   


