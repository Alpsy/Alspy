import urllib2

class HtmlDownloader(object):

    def download(self, new_url):

        if new_url is None:
            return None

        reponse = urllib2.urlopen(new_url)

        if reponse.getcode() != 200:
            return None
        else:
            return reponse.read()