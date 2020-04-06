import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    print('testing testing 123')
    return {'time': time.time()}

@app.route('/')
def index():
    return 'testin'
