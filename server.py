import os
import sqlite3

import falcon
from wsgiref.simple_server import make_server

from base_shooting_stars_resource import BaseShootingStarsResource
os.environ['SHOOTING_STARS_DB'] = '/home/ubuntu/shooting-stars-server/stars.db'
os.environ['SHOOTING_STARS_PORT'] = '8000'


def create_app(conn: sqlite3.Connection, clazz):
    # falcon.App instances are callable WSGI apps
    # in larger applications the app is created in a separate file
    app = falcon.App()

    # Resources are represented by long-lived class instances
    shooting_stars_resource = clazz(conn)

    # things will handle all requests to the '/things' URL path
    app.add_route('/shooting_stars', shooting_stars_resource)
    return app


server_conn = sqlite3.connect(os.environ['SHOOTING_STARS_DB'])
server_conn.row_factory = sqlite3.Row
app = create_app(server_conn, BaseShootingStarsResource)
print(f'Serving on port {os.environ["SHOOTING_STARS_PORT"]}...')
