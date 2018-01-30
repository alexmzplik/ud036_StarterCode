# -*- coding: UTF-8 -*-
import json
from lib.movie import Movie


class Movies(object):
    '''
    Class to create a list of movies.

    attributes:
    _list (array of movie object) -- list container for the movies.
    '''

    def __init__(self):
        self._list = []

    def __repr__(self):
        return 'Movies list({!r})'.format({"Movie": self.items})

    def add(self, value):
        '''
        Adds a movie to the list.
        keyword arguments:
        value   (Movie)  -- the movie title
        TODO: check the way to determine if a variable is an instance of another object or its class type
        '''
        self._list.append(value)

    def index_of(self, name):
        '''
        Returns the position of the Movie in the list after search for its name.
        keyword arguments:
        name (string) -- the movie title/name
        TODO: Find a way to search within the list for a movie by its attribute "title". Maybe use the iterator concept or coroutine?
        '''
        pass

    def delete(self, name):
        '''
        Remove the Movie from the list after search for its name.
        -- Currently not working cause it needs the index_of function
        keyword arguments:
        name (string) -- the movie title/name
        '''
        if name:
            return self._list.remove(self.index_of(name))
        else:
            return False

    def read_csv(self, csv_file):
        '''
        Import the movie list from a csv file
        TODO: learn how to read a csv file quickliy
        '''
        pass

    def read_json(self, json_file):
        '''
        read the data from a json file to create the movie list
        keyword arguments:
        json_file (string) the path to the json file
        '''
        def parse_params(json_element):
            '''
            returns an array of objects to compose a media with ease
            keywords arguments:
            json_element (Object) -- a python object converted from a json element

            attributes:
            title    (string)  -- the media title
            summary  (string)  -- the media summary
            url      (string)  -- the media url
            featured (boolean) -- if the media is featured or not. default false
            '''
            def evaluate(param, else_value=None):
                '''
                check if the given param has value to return or returns an optional value if it has not
                keyword arguments:
                param      (string)  -- the attribute name from the jsn_element
                else_value (variant) -- the value to be used if the attribute has no value. defautl None
                '''
                return else_value if param not in json_element else json_element[param]

            title = evaluate('title')
            summary = evaluate('description')
            url = evaluate('url')
            featured = evaluate('featured', False)
            return title, url, summary, featured

        json_file = json.load(open(json_file, 'r'))
        for json_nodes in json_file:
            movie = Movie(json_nodes['title'],
                          json_nodes['sinopse'], json_nodes['year'])
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
        ''' returns the list of movies regiestered '''
        return self._list

    @property
    def count(self):
        ''' returns the quantity of movies registered '''
        return self._list.count
