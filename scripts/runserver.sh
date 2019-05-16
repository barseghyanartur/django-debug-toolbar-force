#!/usr/bin/env bash
cd examples/simple/
./manage.py runserver --traceback -v 3 --settings=settings.dev "$@"

