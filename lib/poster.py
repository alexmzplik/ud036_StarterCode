# -*- coding: UTF-8 -*-
from lib.media import Media
from lib.validation import Validate


class Poster(Media):
    '''
    Extends the Media class to create a poster object.

    keyword arguments:
    name        (string) -- the poster name
    url         (string) -- the poster image url
    description (string) -- the poster description. Optional

    attributes:
    -- all inherited from Media
    _url (string) -- the image link for the poster
    '''

    def __init__(self, name, url, description=None):
        super(Poster, self).__init__(name, description)
        self._url = url

    def __repr__(self):
        return 'Poster({!r})'.format({
            "name": self.title,
            "description": self.description,
            "url": self.url,
            "created_date": self.created,
            "last_change": self.last_change,
            "url": self.url
        })

    @property
    def url(self):
        ''' returns the link to the poster image '''
        return self._url

    @url.setter
    def url(self, value):
        '''
        define the link for the poster image
        keyword arguments:
        value (string) -- the url link of the poster
        '''
        if Validate.is_valid_url(value):
            self._url = value
