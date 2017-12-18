# -*- coding: UTF-8 -*-
from lib.poster import Poster
from lib.errors import HasNoRecords


class Posters(object):
    def __init__(self):
        self._list = []

    def __repr__(self):
        return 'Poster list ({!r})'.format({"posters": self.list})

    @property
    def list(self):
        ''' Return a copy of the posters registered '''
        return self._list[:]

    @property
    def count(self):
        ''' Return the length of the poster list. '''
        return len(self._list)

    def add(self, name, url, description=None):
        '''
        Add poster to the list
        keyword arguments
        name        (string) -- the title of poster
        url         (string) -- the link for the poster
        description (string) -- details about the poster
        '''
        self._list.append(Poster(name, url, description))
