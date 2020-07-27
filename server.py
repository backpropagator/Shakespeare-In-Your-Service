from bottle import route, run
from predict import *

@route('/<input_line>/<length>')
def index(input_line):
    return {'result': predict(rnn,length,input_line)}

run(host='localhost', port=5533)