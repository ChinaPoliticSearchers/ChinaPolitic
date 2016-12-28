# coding=utf-8
from scrapy import settings
from scrapy.exceptions import IgnoreRequest
from scrapy import extensions


class SqliteDuplicatesFilter(object):
    def __init__(self):
        pass

    def open_domain(self):
        self.fingerprints = set()
        self.init_fingerprints()
        self.sqlite_extension = extensions.enabled['SqliteExtension']

    def close_domain(self):
        self.fingerprints = None

    def enqueue_request(self, domain, request):
        if request.dont_filter:
            return
        fp = self.make_fingerprint(request.url)
        if fp in self.fingerprints:
            raise IgnoreRequest("Skipped Already exists")
        self.fingerprints.add(fp)
        self.sqlite_extension.write_url(self.fingerprints)

    def make_fingerprint(self, url):
        return url

    def init_fingerprints(self):
        fps = map(lambda url: self.make_fingerprint(url), self.sqlite_extension.get_all_exists_url())
        map(lambda fp: self.fingerprints.add(fp), fps)
