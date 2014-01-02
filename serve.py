#!/usr/bin/env python
# coding=utf-8

""" A WSGI app for dev.  """

from cos.app import app

if __name__ == "__main__":
    app.debug = True

    app.run(host='0.0.0.0', port=8887)
