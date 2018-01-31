# -*- coding: UTF-8 -*-
from lib.media import Media
from lib.trailers import Trailers
from lib.posters import Posters


class Movie(Media):
    '''
    Extendends the Media class to create a movie object.

    keyword arguments:
    title   (string)  -- the movie title
    sinopse (string)  -- the movie plot
    year    (integer) -- the year the movie was released

    attributes:
    -- all inherited from Media
    _posters  (array of poster object)  -- a list of posters of the movie
    _trailers (array of trailer object) -- a list of trailers of the movie
    '''

    def __init__(self, title, sinopse, year=None):
        super(Movie, self).__init__(title, sinopse, year)
        self._posters = Posters()
        self._trailers = Trailers()

    def __repr__(self):
        return 'Movie({!r})'.format({
            "title": self.title,
            "sinopse": self.sinopse,
            "year": self.year
        })

    def _nameless_case(self, value, counter):
        '''
        In case the argument value is not defined, it returns an string with
        the movie title and que count attribute of the media it represents
        (trailer or poster)

        keyword arguments:
        value   (string)  -- the title for the media. Optional
        counter (string)  -- the name of attribute with the quantity to be used
        as reference for the media
        '''
        position = getattr(self, counter)
        if value is None or value.strip() == '':
            return '{}_{:0>10}'.format(self.title, position + 1)
        else:
            return value

    def add_poster(self, name, url, description=None):
        '''
        adds poster to the movie.
        keywords arguments:
        name         (string) -- the poster's title
        url          (string) -- the link of the image for the poster
        descriptions (string) -- the poster's description, optional
        '''
        name = self._nameless_case(name, 'posters_count')
        self._posters.add(name, url, description)

    def add_trailer(self, name, url, isFeatured=False):
        '''
        adds poster to the movie.
        keywords arguments:
        name         (string) -- the trailer's title
        url          (string) -- the link of the image for the trailer
        descriptions (string) -- the trailer's description, optional
        '''
        name = self._nameless_case(name, 'trailers_count')
        self._trailers.add(name, url, isFeatured)

    @property
    def trailers(self):
        ''' returns the trailers list '''
        return self._trailers.list

    @property
    def posters(self):
        ''' returns the posters list '''
        return self._posters.list

    @property
    def posters_count(self):
        ''' returns the quantity of posters registered '''
        return self._posters.count

    @property
    def trailers_count(self):
        ''' returns the quantity of trailers registered '''
        return self._trailers.count

    @property
    def featured_trailer(self):
        '''
        returns the featured trailer.
        If there´s no featured trailer, returns the first
        '''
        return self._trailers.featured()
