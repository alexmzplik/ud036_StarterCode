# -*- coding: UTF-8 -*-
class CustomException(Exception):
    def __init__(self):
        super(CustomException, self).__init__(self.message)


class InvalidDate(CustomException):
    def __init__(self, value):
        self.message = "\"%s\" não é uma uma data válida" % value
        super(InvalidDate, self).__init__()


class InvalidURL(CustomException):
    def __init__(self, value):
        self.message = "\"%s\" não é uma um link válido" % value
        super(InvalidURL, self).__init__()


class HasNoRecords(CustomException):
    def __init__(self, value):
        self.message = "\"%s\" não possui registros" % value
        super(HasNoRecords, self).__init__()
