# Didactic Engine Flask

I've worked with Python almost entirely from the maintenance programmer perspective. That is, I take other code written already, make edits, add features, and then redeploy it. I've created exactly zero greenfield applications in Python. That changes today however, with the creation of the didactic-engine-flask app!

## Prerequisites

The only prereq to understanding this article is knowing git, understanding programming in general, and that should be enough. I'm starting this from ground zero. If you're just getting started with Python, be sure to read "[Getting Started With Python Right!](https://compositecode.blog/2019/12/23/getting-started-with-python-right/)" and "[Unbreaking Python Through Virtual Environments](https://compositecode.blog/2019/12/25/unbreaking-python-through-virtual-environments/)" about setting up your environment. These two entries cover enough to ensure you won't end up with broken, conflicted, and convoluted Python environments.

## Mission: Build a Flask based API.

This post is about a singular thing, building an API with Flask. It won't be about data modeling, databases, or wrapping middleware into the fold. It's pure and simple Flask, with just the bare necessities needed to get an API working and responding appropriately requests.

Flask is almost perfect for an example this this because it is a very focused framework. Flask is considered a *microframework*, which fits the mission of this post, as the *micro* in *microframework* is focused on keeping the core simple but extensible. Flask doesn't have tons of convention nor has it pre-made decisions inherent in the framework such as which database or other matters of that sort. The decisions, becasuse of the nature of the framework, are easy to made by us users of the framework because of this core focus.

There are however a few conventions or defaults used in initial configuration of the framework. Templates and static files are stored in subdirectories within the app source tree. The names (by convention) are *templates* and *state*. This can be changed, but these upfront conventions really don't need to be and we can skip over that and get to more important things.

## Flask Installation

I've already setup and have an environment for Python, based on virtualenv setup like I stepped through in [this post](https://compositecode.blog/2019/12/25/unbreaking-python-through-virtual-environments/). The specifics for clarity look like this in my environment.

``` bash
$ python --version
Python 3.7.3
$ which python
/Users/adron/Codez/python-env-examples/bin/python
```

With that activated I stepped right into Flask installation.

``` bash
pip install Flask
```

## First Code

Next up is to write something that executes with Flask. The easiest thing is just creating a standard hello world with a root URL API end point with Flask. To do this I created a file I named `server.py` and added the following code.

``` python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def heyo_mofo():
    return 'Heyo, Sup!'
```

Now export and run this.

``` bash
export FLASK_APP=server.py
flask run
```

This will get the basic application running. If the debugger, automatic reloader, and debug mode is need that can be turned on by setting an environment variable as shown.

``` bash
export FLASK_ENV=development
export FLASK_APP=server.py
flask run
```

## Routing With Routes

Now that I've got a basic hello world working, let's add some more routes that go beyond merely a "heyo sup?". For the next example I'll add 

``` python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/datum')
def hello():
    return 'The data to provide!'

@app.route('/unit/<uuid:unit_id>')
def show_unit(unit_id):
    return 'Unit ID %d, albeit this would usually be used to get the post details and body from a database to present.' % unit_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Showing the subpath after the /path/ - Subpath %s' % escape(subpath)

@app.route('/efforts/')
def projects():
    return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam scelerisque tellus sed magna pulvinar egestas. Donec vitae diam in eros porta mollis. Vestibulum sagittis lorem id dolor luctus, quis tincidunt nulla dictum. Etiam ac vulputate massa. Nullam aliquet arcu imperdiet, mattis mi sed, rutrum lectus. Phasellus viverra leo et mi dapibus tincidunt. Nulla facilisi. Cras eget metus turpis. Etiam a elit arcu. Pellentesque ac eros ligula.'

@app.route('/about')
def about():
    return 'Morbi rhoncus congue justo id malesuada. Mauris semper mattis dui. Etiam sodales dui vitae tincidunt iaculis. Nam id velit accumsan, aliquam lorem ac, ultrices nisl. Aenean non lectus tellus. Mauris rutrum metus ut condimentum efficitur. Nulla a dolor felis. Aenean congue turpis vitae felis commodo, vitae blandit dolor varius. Duis faucibus neque dolor, eu sollicitudin lacus lacinia vel. Etiam hendrerit, nibh vitae porta vestibulum, odio metus sollicitudin justo, in lobortis metus nisi fermentum justo. Cras pellentesque vel nunc posuere fermentum.'
```

Adding detail for each line of code in the routes example above and to start adding some more complete understanding about what is being done by the code. The first `from flask import Flask` line imports the Flask dependency. Next the `app = Flask(__name__)` is assigned by instantiating an instance of the class by passing the `__name__`. Using `__name__` is important because depending on the code being started as an app or imported as a modeul the name is different. This informs Flask where to look for templates, static files, and other collateral.

``` python
from flask import Flask
app = Flask(__name__)
```

The first route listed, shown below cut from the larger code file, calls the `route()` decorator to provide an end point for `127.0.0.1:5000`. This acts as a trigger point for calling the function below, which in this case is defined as `def index():`. Then the return statement provides the response that the function would provide, in this case `return 'Index Page'`.

``` python
@app.route('/')
def index():
    return 'Index Page'
```

The next route is just another route with a sub path for the URL. Instead of just `/`, `/datum` would be the end point to make the request against and the response would be 'The data to provide!'.

``` python
@app.route('/datum')
def hello():
    return 'The data to provide!'
```

Next is use of a converter that is available. Using the `uuid` converter an end point can be made available as shown, which accepts a uuid like this `/unit/5f20697d-1d5f-4773-8047-eaf8a28a94b7` which would then be used to look up a record in a database or some action taken with that uuid. In this example I simply respond with a message that then displays the uuid that was just passed via the URL.

``` python
@app.route('/unit/<uuid:unit_id>')
def show_unit(unit_id):
    return 'Unit ID %d, albeit this would usually be used to get the post details and body from a database to present.' % unit_id
```

One important thing to note is the behavior if a properly formatted uuid is *not* passed in. The response will be a "Not Found", not particular a malformed parameter error.

The next URL route is setup with another converter. This time related to escaping a path.

``` python
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Showing the subpath after the /path/ - Subpath %s' % escape(subpath)
```

When I set this up the first time I actually received an error.

> NameError: name 'escape' is not defined

ADD IMAGE HERE OF ERROR

I did a little research, and looked at some libraries, and found I could add the following to the imports. Once this was added things worked fine.

``` python
from glob import escape
```

### Converters

A quick interuption, here are the converter types available:

| Converter | Description |
|---|---|
| string | (default) accepts any text without a slash |
| int | accepts positive integers |
| float | accepts postive floating point values |
| path | like `string` but also accepts slashes |
| uuid | accepts UUID strings |

As you might note, which I did, that maybe escape isn't a converter included in the Flask converters. I'm not sure which is included where, that is research for another day, but suffice to say it isn't included in the default Flask converters and I needed to pull it from another dependency.

Back to the routes. The next two show the difference in behavior for unique URLs and redirection behavior. The first of the last two routes, the efforts route, has a trailing slash. If access to the URL is requested without the trailing slash Flask then redirects to the canonical URL with the trailing slash.

``` python
@app.route('/efforts/')
def projects():
    return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam scelerisque tellus sed magna pulvinar egestas. Donec vitae diam in eros porta mollis. Vestibulum sagittis lorem id dolor luctus, quis tincidunt nulla dictum. Etiam ac vulputate massa. Nullam aliquet arcu imperdiet, mattis mi sed, rutrum lectus. Phasellus viverra leo et mi dapibus tincidunt. Nulla facilisi. Cras eget metus turpis. Etiam a elit arcu. Pellentesque ac eros ligula.'
```

The next route, the about route, is without a slash at the end of the URL. If a request is made to this URL with a slash, a 404 Not Found error is returned. This forces uniqueness for these resources which in turn helps search engines avoid indexing the same page twice.

``` python
@app.route('/about')
def about():
    return 'Morbi rhoncus congue justo id malesuada. Mauris semper mattis dui. Etiam sodales dui vitae tincidunt iaculis. Nam id velit accumsan, aliquam lorem ac, ultrices nisl. Aenean non lectus tellus. Mauris rutrum metus ut condimentum efficitur. Nulla a dolor felis. Aenean congue turpis vitae felis commodo, vitae blandit dolor varius. Duis faucibus neque dolor, eu sollicitudin lacus lacinia vel. Etiam hendrerit, nibh vitae porta vestibulum, odio metus sollicitudin justo, in lobortis metus nisi fermentum justo. Cras pellentesque vel nunc posuere fermentum.'
```

Mission Accomplished! That was a quick 5 minutes eh! Python is slick like that when combined with frameworks like Flask. Happy thrashing code!

Thanks to [@tlockney](https://twitter.com/tlockney), [@mbbroberg](https://twitter.com/mbbroberg), and [Moshe Zadka](https://twitter.com/moshezadka) so far for ideas around posts, using Python right, and better ways to do things. Watch out, this list could get huge!