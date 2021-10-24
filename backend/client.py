import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')
    sio.emit('subscribe_to_data', "I want to subscribe")


@sio.event
def message(data):
    print('message received with ', data)
    

@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://127.0.0.1:8000')
sio.wait()