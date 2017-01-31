# encoding: utf-8
import url_manager,html_download,html_parser,html_output

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.Urlmanager()    # url管理器对象
        self.download  = html_download.HtmlDownloader() # 网页下载器对象
        self.parser = html_parser.HtmlParse()   # 网页解析器对象
        self.output = html_output.HtmlOutput() # 网页输出对象

    def craw(self,root):
        count = 1
        self.urls.add_new_url(root) # 加入初始的url作为入口

        while self.urls.has_new_url():

            try:
                new_url = self.urls.get_url()   # 从url管理器获取待爬取的url
                print 'craw %d:%s' %(count,new_url)
                html_cont = self.download.download(new_url) # 下载待爬取url的html页面
                new_urls,new_data = self.parser.parse(new_url,html_cont)    # 解析已经下载的页面，获取新的待爬取的url和有价值数据
                self.urls.add_new_urls(new_urls)    # 将新的待爬取的url加入url管理器
                self.output.collect_data(new_data)  # 收集数据

                if count == 10:   # 爬取1000个条目结束爬取
                    break

                count = count + 1

            except :
                print 'craw failed'

        self.output.output_html()   # 输出内容



if __name__ == '__main__':
    url_entrance = 'http://baike.baidu.com/link?url=jqYWWY0bp7WNcMbXzQc7DiuaaIvFZK6sMx2YiAvI7VfAkAQ9JTiUHf3GoS5d58h6v4GJlhlzT-35rrkp6yFlLK'
    obj_spider = SpiderMain()
    obj_spider.craw(url_entrance)
