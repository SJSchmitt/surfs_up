# import dependencies
from flask import Flask

# create app instance
app = Flask(__name__)
@app.route('/')

# test function
def hello_world():
    return 'Hello world'