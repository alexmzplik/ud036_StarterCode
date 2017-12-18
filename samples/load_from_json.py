# -*- coding: UTF-8 -*-
from datetime import datetime
from lib.movies import Movies
import time

def show_basic_info(movie_list):
    for movie in movie_list:
        print movie.title, movie.year, movie.trailers, movie.featured_trailer

shelf = Movies()
json_file = 'data/movies.json'
print '-- importando do arquivo', json_file
shelf.read_json(json_file)
print '--', json_file, 'importado'
time.sleep(5)
print '-- exibindo posters do primeiro filme da lista'
print shelf.items[0].posters
print '-- exibindo um trailer do primeiro filme da lista'
print shelf.items[0].trailers[0]
time.sleep(5)
print '-- alterando data de criação desse trailer'
shelf.items[0].trailers[0].created = datetime.now()
print '-- exibindo um trailer do primeiro filme da lista, com data alterada'
print shelf.items[0].trailers[0]
time.sleep(5)
print '-- exibindo todos os registros importados'
show_basic_info(shelf.items)
