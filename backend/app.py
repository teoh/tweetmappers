from tornado import websocket, web, ioloop
import json

cl = set()

class SocketHandler(websocket.WebSocketHandler):
    
    def check_origin(self, origin):
        return True

    def open(self):
	print "open"
        if self not in cl:
            cl.add(self)

    def on_close(self):
        print "close"
	if self in cl:
            cl.remove(self)

def write(message):
    [con.write_message(message) for con in cl]

app = web.Application([
    (r'/ws', SocketHandler),
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
