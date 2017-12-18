# -*- coding: UTF-8 -*-
from webbrowser import open as OpenBrowser
from os.path import abspath as AbsolutePath
from lib.movies import Movies

def youtube_id_from_trailer(url):
    from re import search as regex_search
    result = regex_search(r'(?<=v=)[^&#]+', url)
    result = result or regex_search(r'(?<=be/)[^&#]+', url)
    return result.group(0) if result else None

def create_movie_tiles_content(movies):
    movie_tile_content = open('model/movie_tile.html', 'r').read()
    content = ''
    for movie in movies:
        trailer_youtube_id = youtube_id_from_trailer(movie.featured_trailer.url)
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.posters[0].url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
    header = open('model/header.html', 'r').read()
    body = open('model/body.html', 'r').read()
    output_file = open('fresh_tomatoes.html', 'w')
    rendered_content = body.format(movie_tiles=create_movie_tiles_content(movies))
    
    output_file.write(header + rendered_content)
    output_file.close()
    url = AbsolutePath(output_file.name)
    OpenBrowser('file://' + url, new=2)

shelf = Movies()
movies_json = 'data/movies.json'
shelf.read_json(movies_json)
open_movies_page(shelf.items)
