import requests
from lxml import html

class duckduckgo(object):
    def __init__(self):
        self.url = []
        self.result = ''

    def search(self,query,s=0,dc=0,nextParams=None):
        self.query = query
        url = 'https://duckduckgo.com/html/'
        params = {'q':query,'dc':dc,'s':s,'nextParams':nextParams,'v':'l','o':'json','api':'/d.js'}
        r = requests.post(url,data=params)
        tree = html.fromstring(r.content)
        result = self.find(tree)
        if self.result:
            return self.result

    def find(self,tree):
        links,nextParams,s,dc = [tree.xpath('//*[@id="links"]/div/div/h2/a/@href'),tree.xpath('//*[@class="nav-link"]/form/input[4]/@value'),tree.xpath('//*[@class="nav-link"]/form/input[3]/@value'),tree.xpath('//*[@class="nav-link"]/form/input[7]/@value')]
        for link in links:
            self.url.append(link)
        if len(s) == 1:
            self.search(self.query,s=s[0],dc=dc[0],nextParams=nextParams[0])
        elif len(s) >= 2:
            self.search(self.query,s=s[1],dc=dc[1],nextParams=nextParams[0])
        else:
            self.result = self.url

if __name__ == '__main__':
    dd = duckduckgo()
    urls = dd.search('pythonicos')
    for url in urls:
        print url
