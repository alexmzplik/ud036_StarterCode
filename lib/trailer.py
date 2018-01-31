# -*- coding: UTF-8 -*-
from lib.validation import Validate
from lib.media import Media


class Trailer(Media):
    '''
    Extendends the Media class to create a trailertrailer object.

    keyword arguments:
    title        (string)   -- the trailer title
    sinopse      (string)   -- the trailer plot
    release_date (timestap) -- the date the trailer was released

    attributes:
    -- all inherited from Media
    _url  (array of poster object)  -- the url to the trailer
    _released (array of trailer object) -- the trailer release date
    '''

    def __init__(self, title, url, release_date=None):
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
        ''' returns the url to the trailer '''
        return self._url

    @url.setter
    def url(self, value):
        '''
        define the link for the trailer

        keyword arguments:
        value (string) -- the url for the trailer
        '''
        if Validate.is_valid_url(value):
            self._url = value

    @property
    def release_date(self):
        ''' returns the date when the trailer was released'''
        return self._released

    @release_date.setter
    def release_date(self, value):
        '''
        define the release dat for the trailer
        keyword arguments:
        value (timestamp) -- the date when the trailer was released
        '''
        self._released = value
