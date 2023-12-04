from flask import Flask
from search4letters import search4words


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/search')
def do_search() ->str:
    return str(search4words('My name is danany',set('arei')))

app.run()
