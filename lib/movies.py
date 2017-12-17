# -*- coding: UTF-8 -*-
import json
from lib.movie import Movie

class Movies(object):
    def __init__(self):
        self._list = []

    def __repr__(self):
        return 'Movies list()'

    def add(self, value):
        self._list.append(value)

    def index_of(self, name):
        #TODO: search by name of movie
        pass

    def delete(self, name):
        if name:
            return self._list.remove(self.index_of(name))
        else:
            return False

    def _read(self, archive):
        return open(archive, 'r')

    def read_json(self, file):
        _ = json.load(self._read(file))
        for node in _:
            movie = Movie(node['title'], node['sinopse'], node['year'])
            if len(node['trailers']) > 0:
                for trailer in node['trailers']:
                    movie.add_trailer(
                        trailer['title'], trailer['url'], ('featured' in trailer))
            if len(node['posters']) > 0:
                for poster in node['posters']:
                    movie.add_poster(poster['url'], poster['description'])
            self.add(movie)

    @property
    def items(self):
        return self._list
