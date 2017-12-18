# -*- coding: UTF-8 -*-
from lib.media import Media
from lib.trailers import Trailers

class Movie(Media):
    def __init__(self, title, sinopse, year=None):
        super(Movie, self).__init__(title, sinopse, year)
        self._posters = []
        self._trailers = Trailers()
    
    def __repr__(self):
        return 'Movie({!r})'.format({
            "title": self.title,
            "sinopse": self.sinopse,
            "year": self.year
        })
    
    def add_poster(self, url, description = None):
        pass

    def add_trailer(self, name, url, isFeatured=False):
        ''' adds a trailer to the trailer list '''
        self._trailers.add(name, url, isFeatured)
    
    @property
    def trailers(self):
        ''' list all trailers from the list '''
        return self._trailers.list

    @property
    def trailers_count(self):
        ''' Return the length of the trailer list '''
        return self._trailers.count
    
    @property
    def featured_trailer(self):
        return self._trailers.featured()
