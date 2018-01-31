# -*- coding: UTF-8 -*-
from webbrowser import open as OpenBrowser
from os import makedirs as MakeDir
from os.path import exists, abspath as AbsolutePath
from lib.movies import Movies


def youtube_trailer_id(url):
    '''
    Extrai o id do vídeo no youtube

    Argumentos-chave:
    url -- link para o vídeo
    '''
    from re import search as regex_search
    result = regex_search(r'(?<=v=)[^&#]+', url)
    result = result or regex_search(r'(?<=be/)[^&#]+', url)
    return result.group(0) if result else None


def create_movie_tiles_content(movies):
    ''''
    Popula o bloco dos filmes para a página

    Argumentos-chave:
    movies -- lista com filmes criada com a classe Movie
    '''
    movie_tile_content = open('model/movie_tile.html', 'r').read()
    content = ''
    for movie in movies:
        trailer_youtube_id = youtube_trailer_id(movie.featured_trailer.url)
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.posters[0].url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies, html_page):
    ''''
    Cria a página de filmes a a abre no browser

    Argumentos-chave:
    movies -- lista com filmes criada com a classe Movie
    '''
    output_dir = 'output/'
    html_file = '{}/{}.html'.format(output_dir, html_page)
    try:
        output_file = open(html_file, 'w')
        if not exists(AbsolutePath(output_dir)):
            MakeDir(output_dir)

        header = open('model/header.html', 'r').read()
        body = open('model/body.html', 'r').read()
        footer = open('model/footer.html', 'r').read()
        rendered_content = body.format(movie_tiles=create_movie_tiles_content(
            movies))

        output_file.write(header + rendered_content + footer)
        output_file.close()
        url = AbsolutePath(output_file.name)
        OpenBrowser('file://' + url, new=2)
    except NameError as error:
        print "Não foi possível criar a página {}" % html_file
        print type(error)
        print error.args
        print error
