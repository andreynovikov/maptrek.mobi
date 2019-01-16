#!/usr/bin/python3

import json
import psycopg2
import psycopg2.extras
from webob import Request, Response

import wsgiref.handlers

import config


def application(environ, start_response):
    request = Request(environ)

    data = []

    db = psycopg2.connect(config.DB_GIS_CONNECTION_DSN)
    cursor = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute('''SELECT * FROM trekarta_stats''')

    for row in cursor:
        del row['at']
        data.append(row)

    cursor.close()

    response = Response(json=data)
    response.cache_expires(0)
    response.cache_control.private = True
    return response(environ, start_response)


if __name__ == '__main__':
    wsgiref.handlers.CGIHandler().run(application)
