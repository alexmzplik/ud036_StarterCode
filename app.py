# -*- coding: UTF-8 -*-
from lib.movies import Movies
from lib.page_creator import open_movies_page

''' here we instante the Movies Class '''
shelf = Movies()

''' here we read the json file with the movies '''
shelf.read_json('data/movies.json')

'''
  here we call the function open_movies_page giving the
  items property from the Movies class object and a name
  to the file it will create.
  After created, the file will be opened on the browser
'''
open_movies_page(shelf.items, 'fresh_tomatoes')
