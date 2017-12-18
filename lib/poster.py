# -*- coding: UTF-8 -*-
from lib.media import Media
from lib.validation import Validate

class Poster(Media):
    def __init__(self, name, url, description = None):
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
        return self._url

    @url.setter
    def url(self, value):
        if Validate.is_valid_url(value):
            self._url = value
