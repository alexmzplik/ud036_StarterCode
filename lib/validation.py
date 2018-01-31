# -*- coding: UTF-8 -*-
from re import compile, IGNORECASE, error as re_error
from errors import InvalidURL, InvalidDate, InvalidYear
from datetime import datetime, date


class Validate(object):
    @staticmethod
    def is_valid_url(value):
        '''
        check if the keyword argument value (string) is a valid url
        using regular expression
        '''
        regex = compile(r'^(?:http|ftp)s?://'
                        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)' +
                        '+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                        r'localhost|'
                        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                        r'(?::\d+)?'
                        r'(?:/?|[/?]\S+)$', IGNORECASE)
        if regex.search(value):
            return True
        else:
            raise InvalidURL(value)

    @staticmethod
    def is_valid_date(value):
        '''
        check if the keyword argument value (string) is a validade a date
        '''
        try:
            datetime.strftime(value, '%Y-%m-%d')
        except ValueError:
            raise InvalidDate(value)

    @staticmethod
    def is_valid_year(year):
        '''
        check if the keyword argument value (string) is a valid a year
        TODO: it's only checking if the value is a number and is higher than
        zero, so we need to discover a better way to determine what a year
        represents.
        '''
        regex = compile(r'^\d+$')
        if regex.search(str(year)) and year > 0:
            return True
        else:
            raise InvalidYear(year)
