# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import time

from threading import Thread
from flask_socketio import SocketIO, emit, join_room, disconnect

app = Flask(__name__,static_url_path='/files',static_folder='static',template_folder='static')

socketio = SocketIO(app)
thread = None

ti=time.time()
def background_stuff():
    """ Let's do it a bit cleaner """
    global ti
    while True:
        time.sleep(1)
        t = str(time.time()-ti)
	socketio.emit('message', {'data': 'This is data', 'time':'Started at '+ t + ' sec'}, namespace='/test')


@app.route('/')
def index():
    global thread,ti
    ti=time.time()
    if thread is None:
        thread = Thread(target=background_stuff)
        thread.start()
    
    return render_template('index.html')


@socketio.on('my event', namespace='/test')
def my_event(msg):
    print msg['data']

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	print('Client disconnected')

if __name__ == '__main__':
	socketio.run(app,debug=True)

