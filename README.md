# The Fresh Tomatoes project
- [Fresh Tomatoes](#fresh-tomatoes)
    - [What is this?](#what-is-this)
    - [How to use](#how-to-use)
    - [The components](#the-components)
        - [Data](#data)
            - [JSON file structure:](#json-file-structure)
        - [Layout template](#layout-template)
        - [Classes and Functions](#classes-and-functions)
- [There's always ways to improve](#theres-always-ways-to-improve)

## What is this?
This project is an exercise of a movie trailer website file creation in python using template and objects for my *Web Full-Stack nanodegree program* course.

## How to use
All we need is an json file as in [json structure](#data), import the *Movies class* and the *open_movies_page function*, instanciate Movies and import the json file and call *open_movies_page*.

Below we have the sample of file to create the page:

```python
# app.py file
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
```

## The components
Or, if you preffer, "the boring stuff"
### Data
In the folder *./data* the *movies.json* file has a exemple of the data needed to our app.
#### JSON file structure:
```javascript
// movies.json
{
        "title": "the movie title",
        "sinopse": "the plot of movie",
        "year": "the year it was produced",
        "posters": [{/*a list of posters of this movie*/
            "url": "a link to the image",
            "description": "some text about it, optional"
        }],
        "trailers": [{/*list of trailers*/
            "title": "trailer title, like official trailer, redband, etc.",
            "url": "the link to the video"
            "featured": "a boolean value to define if this shoul be the first trailer to show"
        }]
    }
```
### Layout template
in the folder */model* whe have the templates that compose the webpage.
* **header.html**: here we have the page title and the site header
* **body.html**: here we have the layout of the main page content and the modal for video exibition
* **movie_tile**: the tile which will be visible in the modal from *body.html*.
* **footer.html**: the footer part of the page.

### Classes and Functions
The classes and functions of this project are in the *./lib* folder.
* **errors**: Here we have some custom exceptions.
* **media**: the class for a generic object with title/name, description, year, creation date and last changed properties.
* **movie**: the class for creating a movie object. It inherits properties from the *Media class* object and uses instaces of the *Trailers list* and the *Posters list* objects.
* **movies**: the class for creating a list of movies. it has properties to get the featured trailer.
* **page_creator**: the functions to combine the *[layout templates](#layout-template)* with an instace of *Movies* class.
* **poster**: the class for creating a *Poster* object. It inherits properties from the *Media class object* 
* **posters**: the class for creating a list of *Poster* objects.
* **trailer**: the class for creating a *Trailer* object. It inherits properties from the *Media class* object.
* **trailers**: the class for creating a list of *Trailer* objects.
* **validation**: the class to check properties and call the custom errors if needed.

# There's always room to improve
Today, this project uses errors and messages in brazilian portuguese, which is my mother language. Also it has some decisions in the code that I'm not satisfied, but work nonetheless.
I'm still learning python and this project is a study of that.
So the next steps for this project can be:
* A way the langage of the error messages
* A queue line to play the other trailers
* A gallery of posters
* An about the movie to show its information
* Select a movie by name
* Keep track of the update of the movie properties
* Access and save to other types of data (DBMS, csv file or API)
* How about forget the file creation and do a full server side application?
