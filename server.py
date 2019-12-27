from flask import Flask
from glob import escape
app = Flask(__name__)

# global escape: true

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