# -*- coding: UTF-8 -*-

class Media(object):
    def __init__(self, title, sinopse, year=None):
        self._title = title
        self._sinopse = sinopse
        self._year = year

    @property
    def title(self):
        return self._title

    @property
    def sinopse(self):
        return self._sinopse

    @property
    def year(self):
        return self._year