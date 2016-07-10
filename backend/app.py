from tornado import websocket, web, ioloop
import json

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

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
