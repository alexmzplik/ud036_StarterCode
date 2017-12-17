# -*- coding: UTF-8 -*-
from validation import Validate
from datetime import datetime

class Trailer(object):
    def __init__(self, title, url, date_release = None):
        self._title = title
        self._url = None
        self._released = date_release

        self.url = url
        self._inserted_date = datetime.now()
        self.__has_changed()

    def __repr__(self):
        return 'Trailer({!r})'.format({
            "title": self.title,
            "url": self.url,
            "last_change": self.last_change
        })

    def __has_changed(self):
        self._last_change = datetime.now()
    
    @property
    def last_change(self):
        return self._last_change#.isoformat()

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def url(self):
        return self._url
    @url.setter
    def url(self, value):
        if Validate.is_valid_url(value):            
            self._url = value

    @property
    def date_release(self):
        ''' Retun the date when the trailer was released'''
        return self._released

    @property
    def created(self):
        ''' Retun the date when the trailer was registered'''
        return self._inserted_date
