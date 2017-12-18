# -*- coding: UTF-8 -*-
from lib.validation import Validate
from lib.media import Media

class Trailer(Media):
    def __init__(self, title, url, release_date = None):
        super(Trailer, self).__init__(title, None)
        self._url = url
        self._released = release_date

    def __repr__(self):
        return 'Trailer({!r})'.format({
            "title": self.title,
            "url": self.url,
            "release_date": self.release_date,
            "created_date": self.created,
            "last_change": self.last_change
        })

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if Validate.is_valid_url(value):           
            self._url = value

    @property
    def release_date(self):
        ''' Retun the date when the trailer was released'''
        return self._released

    @release_date.setter
    def release_date(self, value):
        self._released = value
