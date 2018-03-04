# -*- coding: utf-8 -*-

'''
Created on May 12, 2017

@author: Jzzz
'''
import re
import requests





class PdfDownload(object):
    def get_pdf(self,catch,soup,html):
        url = 'http://www.dailywell.com.tw/'
#     catch='http://www.dailywell.com.tw/s/2/product-465210/Miniature-Toggle-Switches-1M-Series.html'


        html = requests.get(catch).text
#         soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
#print html
        pdf_url=re.findall('<a\s*href\s*="?(\S+).pdf"',html,re.S)
        name=soup.find('h1',class_="name")
        if name:
            name = name.get_text()
        if pdf_url:
            if name.find(' '):
                name=re.sub('\s','',name)
                name=re.sub('\r\n','',name)
                name=re.sub(',','',name)
            
                print name
            for each in pdf_url:
   
    
                judge=each.find("../../../c")
                if judge!=-1:
                    each=each.replace("../../../",url)+".pdf"
#                     each=each+".pdf"
                    print each
                pdf=requests.get(each,timeout=10)

                string = 'pdf\\'+' '+name+'.pdf'
                fp = open(string,'wb')
                fp.write(pdf.content)
                fp.close()
  


