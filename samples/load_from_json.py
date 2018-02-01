# -*- coding: UTF-8 -*-
from datetime import datetime
from lib.movies import Movies
import time


def show_basic_info(movie_list):
    '''
    a simple test to show basic info from the Movies Object

    Arguments:
    movie_list (Movies) container with a list of Movie object
    '''
    for movie in movie_list:
        print movie.title, movie.year, movie.trailers, movie.featured_trailer


'''
this file is a simple exemple of how to extract the data from json file
and some simple manipulation of the Movies object

Here we instatiate the Movies Object
'''
shelf = Movies()
'''
then we set a variable with the json file to import the movies info
to the Movies container
'''
json_file = 'data/movies.json'

print '-- importando do arquivo', json_file
'''
importing the data from the json file
'''
shelf.read_json(json_file)
print '--', json_file, 'importado'
time.sleep(5)
print '-- exibindo posters do primeiro filme da lista'
'''
printing the list of posters from the first movie extracted from the json file
'''
print shelf.items[0].posters
print '-- exibindo um trailer do primeiro filme da lista'
'''
printing the info from the first trailer from the first movie
'''
print shelf.items[0].trailers[0]
time.sleep(5)
print '-- alterando data de criação desse trailer'
'''
changing the release date from the first trailer
'''
shelf.items[0].trailers[0].release_date = datetime.now()
print '-- exibindo um trailer do primeiro filme da lista, com data alterada'
'''
printing the trailer info so we can confirm that the release date has changed
'''
print shelf.items[0].trailers[0]
time.sleep(5)
print '-- exibindo todos os registros importados'
'''
calling the function to expose the basic info from all movies we imported
'''
show_basic_info(shelf.items)
