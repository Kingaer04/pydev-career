from search4letters import search4words
from flask import Flask


app = Flask(__name__)

@app.route('/search4')

def do_search() ->str:
    return str(search4words("my name is dananny and i will become the greatest programmer ever", set("aios")))

app.run()    