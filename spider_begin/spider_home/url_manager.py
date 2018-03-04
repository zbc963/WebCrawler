
import urllib2




class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.old_urls.add('http://www.dailywell.com.cn')
        self.old_urls.add('http://www.dailywell.com.tw/?lang=1&TTo=zh-tw')
        self.old_urls.add('http://www.dailywell.com.tw/?lang=2&TTo=es')
        self.old_urls.add('http://www.dailywell.com.tw/?lang=2&TTo=ru')
        self.old_urls.add('http://www.dailywell.com.tw/?lang=2&TTo=fr')
        self.old_urls.add('http://www.dailywell.com.tw/?lang=2&TTo=fr')
        self.old_urls.add('http://www.dailywell.com.tw/s/2/news-c2601/%E5%B1%95%E8%A6%BD%E8%B3%87%E8%A8%8A.html')

     
    def add_new_url(self, url):
        url = urllib2.quote(url.encode('utf-8'))
        url=url.replace('%3A',':')
        if url is None:
            return
#         for each in self.old_urls:
#             print each
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(str(url))

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
