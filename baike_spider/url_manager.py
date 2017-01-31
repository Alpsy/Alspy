# encoding:utf-8
class Urlmanager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 提交一个url到url管理器
    def add_new_url(self, root):
        if root is None:
            return
        if root not in self.new_urls or root not in self.old_urls:  # 不再待爬取或者已经爬取的容器中，说明是新的url，加入
            self.new_urls.add(root)

    # 批量提交url到url管理器
    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls)==0:
            return

        for url in new_urls:
            self.new_urls.add(url)

    # 判断管理器中是否含有待爬取的url
    def has_new_url(self):
       return len(self.new_urls) != 0

    # 从管理器中获取新的url
    def get_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
