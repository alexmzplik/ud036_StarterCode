# -*- coding: UTF-8 -*-
from lib.trailer import Trailer
from lib.errors import HasNoRecords

class Trailers(object):
    def __init__(self):
        self._list = []
        self._featured = 0

    def __repr__(self):
        return 'Trailer list ({!r})'.format({"trailers": self.list})

    # TODO: implementar validação
    def __is_trailer(self, name, url):
        return True

    @property
    def list(self):
        ''' Return a copy of the trailers registered '''
        return self._list[:]

    @property
    def count(self):
        ''' Return the length of the trailer list. '''
        return len(self._list)

    def add(self, name, url, isFeatured=False):
        '''
        Add trailer to the list
        keyword arguments
        name       (string)  -- the title of trailer strign
        url        (string)  -- the link for the trailer
        isFeatured (boolean) -- if the the trailer is the principal to show
        '''
        if self.__is_trailer(name, url):
            item = Trailer(name, url)
            self._list.append(item)
        if isFeatured:
            self._featured = len(self._list) -1

    def featured(self):
        '''
        Return featured trailer.
        If not defined get the first one
        '''
        if self.count == 0:
            raise HasNoRecords("The trailer list")
        return self._list[self._featured]
