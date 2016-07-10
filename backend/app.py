import json

from tornado import websocket, web, ioloop
from threading import Thread

cl = set()

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        cl.add(self)

    def on_close(self):
        cl.remove(self)

def write(message):
    print 'Sending...'
    [con.write_message(message) for con in cl]
    print 'Success!'
    print '############## Connections ##################'
    print cl
    print '############## Cool! ##################'

app = web.Application([
    (r'/ws', SocketHandler),
])

def main():
    app.listen(8888)
    ioloop.IOLoop.instance().start()

my_thread = Thread(main)
my_thread.start()
