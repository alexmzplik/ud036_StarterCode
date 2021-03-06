# The Fresh Tomatoes project
- [The Fresh Tomatoes project](#the-fresh-tomatoes-project)
    - [What is this?](#what-is-this)
    - [How to use](#how-to-use)
        - [What is Love, I mean, Python?](#what-is-love-i-mean-python)
        - [Yes, I now python-fu!](#yes-i-now-python-fu)
    - [The components](#the-components)
        - [Data](#data)
            - [JSON file structure:](#json-file-structure)
        - [Layout template](#layout-template)
        - [Classes and Functions](#classes-and-functions)
- [There's always room to improve](#theres-always-room-to-improve)

## What is this?

This project is an exercise of a movie trailer website file creation in python using template and objects for my _Web Full-Stack nanodegree program_ course.

## How to use

### What is Love, I mean, Python?

If you want test this, you need Python. You doesn't know Python, then your new best friend will be this link https://www.python.org/about/gettingstarted/.
Once you have Python installed, running and tried some new tricks, you can download this and on your favorite shell go to the folder where you save and run the app.py file

```
$ python app.py
```

The result can be viewed on **./output/fresh_tomatoes.html**, which will be open on the browser.

### Yes, I now python-fu!

Then all you need is an json file as in [json structure](#data), import the _Movies class_ and the _open_movies_page function_, instanciate Movies and import the json file and call _open_movies_page_.

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

The result can be viewed on **./output/fresh_tomatoes.html**

## The components

Or, if you preffer, "the boring stuff" [wink and smile]

### Data

In the folder _./data_ the _movies.json_ file has a exemple of the data needed to our app.

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

in the folder _/model_ whe have the templates that compose the webpage.

* **header.html**: here we have the page title and the site header
* **body.html**: here we have the layout of the main page content and the modal for video exibition
* **movie_tile**: the tile which will be visible in the modal from _body.html_.
* **footer.html**: the footer part of the page.

### Classes and Functions

The classes and functions of this project are in the _./lib_ folder.

* **errors**: Here we have some custom exceptions.
* **media**: the class for a generic object with title/name, description, year, creation date and last changed properties.
* **movie**: the class for creating a movie object. It inherits properties from the _Media class_ object and uses instaces of the _Trailers list_ and the _Posters list_ objects.
* **movies**: the class for creating a list of movies. it has properties to get the featured trailer.
* **page_creator**: the functions to combine the _[layout templates](#layout-template)_ with an instace of _Movies_ class.
* **poster**: the class for creating a _Poster_ object. It inherits properties from the _Media class object_. It was based on the file fresh_tomatoes.py from the udacity/ud036_StarterCode repository
* **posters**: the class for creating a list of _Poster_ objects.
* **trailer**: the class for creating a _Trailer_ object. It inherits properties from the _Media class_ object.
* **trailers**: the class for creating a list of _Trailer_ objects.
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
