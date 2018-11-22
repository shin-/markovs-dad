import os

from gevent.pywsgi import WSGIServer

from .app import flask_app, populate_generator

if __name__ == '__main__':
    populate_generator(use_cache=os.environ.get('USE_CACHE') == 'true')
    server = WSGIServer(('0.0.0.0', 5000), flask_app)
    server.serve_forever()
