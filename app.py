# -*- coding: utf-8 -*-
import cherrypy
import json
import os
import requests

from urllib.parse import urlparse, urlencode
from newsplease import NewsPlease


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return str(obj)


class NewsParserAPI(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def default(self, *args, **params):
        response = {}

        if 'url' in params:
            article = NewsPlease.from_url(params['url'])
            response = article.get_dict()

        response = json.loads(json.dumps(response, cls=DatetimeEncoder))

        return response

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    },
    '/assets': {
        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'assets',
    }
}

cherrypy.quickstart(NewsParserAPI(), '/', config=config)
