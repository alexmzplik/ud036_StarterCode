# -*- coding: UTF-8 -*-
from datetime import datetime
from lib.validation import Validate

class Media(object):
    def __init__(self, title, sinopse, year=None):
        self._title = title
        self._sinopse = sinopse
        self._year = year
        self._inserted_date = datetime.now()
        self._last_change = datetime.now()

    @property
    def title(self):
        return self._title

    @property
    def name(self):
        return self._title

    @property
    def description(self):
        return self._sinopse

    @property
    def sinopse(self):
        return self._sinopse

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if Validate.is_valid_year(value):
            self._year = value

    @property
    def last_change(self):
        return self._last_change

    @property
    def created(self):
        return self._inserted_date
    
    @created.setter
    def created(self, value):
        if Validate.is_valid_date(value):
            self._inserted_date = value
