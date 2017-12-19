# -*- coding: UTF-8 -*-
import json
from lib.movie import Movie

class Movies(object):
    def __init__(self):
        self._list = []

    def __repr__(self):
        return 'Movies list({!r})'.format({"Movie": self.items})

    def add(self, value):
        self._list.append(value)

    def index_of(self, name):
        #TODO: criar a busca por nome do filme.
        # usar iterator ou coroutine? 
        pass

    def delete(self, name):
        if name:
            return self._list.remove(self.index_of(name))
        else:
            return False

    def read_csv(self, csv_file):
        #TODO: a reader from csv file
        pass

    def read_json(self, json_file):
        def parse_params(json_element):
            def evaluate(param, else_value=None):
                return else_value if param not in json_element else json_element[param]

            title = evaluate('title')
            summary = evaluate('description')
            url = evaluate('url')
            featured = evaluate('featured', False)
            return title, url, summary, featured

        json_file = json.load(open(json_file, 'r'))
        for json_nodes in json_file:
            movie = Movie(json_nodes['title'], json_nodes['sinopse'], json_nodes['year'])
            if 'trailers' in json_nodes:
                for trailer in json_nodes['trailers']:
                    attr = parse_params(trailer)
                    movie.add_trailer(attr[0], attr[1], attr[3])
            if 'posters' in json_nodes:
                for poster in json_nodes['posters']:
                    attr = parse_params(poster)
                    movie.add_poster(attr[0], attr[1], attr[2])
            self.add(movie)

    @property
    def items(self):
        return self._list

    @property
    def count(self):
        return self._list.count
