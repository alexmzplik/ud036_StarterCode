# -*- coding: UTF-8 -*-
from datetime import datetime
from lib.validation import Validate


class Media(object):
    '''
    Base class for any type of media like movie, poster, trailer, book, etc.
    keyword arguments:
    title   (string)  -- the title/name for the media.
    sinopse (string)  -- the description of the media.
    year    (integer) -- year when it was published or released, optional.

    attributes:
    _title       (string)   -- the title/name of the media.
    _name        (string)   -- a shortcut to the title of the media.
    _sinopse     (string)   -- the description of the media.
    _year        (integer)  -- year when the media was published or released.
    _created     (datetime) -- the date when the media object was created.
    _last_change (datetime) -- the date of the last change of the media.
    '''

    def __init__(self, title, sinopse, year=None):
        self._title = title
        self._sinopse = sinopse
        self._year = year
        self._inserted_date = datetime.now()
        self._last_change = datetime.now()

    @property
    def title(self):
        ''' returns the media title '''
        return self._title

    @property
    def name(self):
        ''' an alias to the media title '''
        return self._title

    @property
    def description(self):
        '''returns the media plot / story '''
        return self._sinopse

    @property
    def sinopse(self):
        '''an alias to the media plot '''
        return self._sinopse

    @property
    def year(self):
        ''' returns the year the media was released '''
        return self._year

    @year.setter
    def year(self, value):
        '''
        define the year the media was relesased
        keywords arguments:
        value (integer) -- the media year of release
        '''
        if Validate.is_valid_year(value):
            self._year = value

    @property
    def last_change(self):
        ''' returns the date of the last update of the media properties '''
        return self._last_change

    @property
    def created(self):
        ''' returns the date the media object was created '''
        return self._inserted_date

    @created.setter
    def created(self, value):
        '''
        define the date of creation of the media object
        keyword arguments:
        value (datetime) -- the date when the media object is created
        '''
        if Validate.is_valid_date(value):
            self._inserted_date = value
