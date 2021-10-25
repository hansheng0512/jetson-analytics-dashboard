import uuid

import eventlet
import socketio
import time
import json

sio = socketio.Server(cors_allowed_origins=['http://localhost:3000'])
app = socketio.WSGIApp(sio)
clients = []


@sio.event
def connect(sid, environ):
    print('connect ', sid)
    # subscribe(sid, 'hello world')
    # sio.enter_room(sid, 'chat_users')
    clients.append(sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    # sio.leave_room(sid, 'chat_users')
    clients.remove(sid)


def my_message(sid, data):
    sio.emit('data', data)
    print('Send message ', data, sid)


@sio.on("getData")
def get_data(sid):
    data = {}
    with open('data.txt') as json_file:
        data = json.load(json_file)
    my_message(sid, data)
    sio.sleep(0.1)

# @sio.event
# def my_message(sid, data):
#     sio.emit('data', data)
#     print('Send message ', data, sid)


# @sio.on('subscribe_to_data')
# def subscribe(sid, data):
#     # counter = 0
#     while len(clients) > 0:
#         try:
#             # f = open("demofile3.txt", "r")
#             # counter = f.read()
#             data = {}
#             with open('data.txt') as json_file:
#                 data = json.load(json_file)
#             # counter += 1
#             my_message(sid, data)
#             sio.sleep(0.1)
#         except:
#             pass


eventlet.wsgi.server(eventlet.listen(('localhost', 8000)), app)
