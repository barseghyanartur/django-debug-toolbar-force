#!/usr/bin/env bash
reset
pycodestyle examples/simple/ --exclude examples/simple/wsgi.py,migrations,south_migrations
