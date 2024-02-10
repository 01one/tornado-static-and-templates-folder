import tornado.web
from tornado.options import define, options, parse_command_line
import tornado.ioloop
import os
import logging


define("port", default=5000, help="port number", type=int)
define("debug", default=True, help="debug mode")

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        return self.render('index.html')

def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=options.debug,
    )
    app.listen(options.port)
    logging.info(f"Server running on port {options.port}, debug mode: {options.debug}")
    
    logging.info(f"http://localhost:{options.port}")
    
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
