# -*- coding: utf-8 -*-

import requests
import tornado.web
import tornado.ioloop

import api

PORT = 8888
URLS = [
        (r"/cep/$", api.CEPResource.as_list()),
        (r"/cep/([^/]+)", api.CEPResource.as_detail()),
    ]

if __name__ == "__main__":
    app = tornado.web.Application(URLS, debug=True)
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
