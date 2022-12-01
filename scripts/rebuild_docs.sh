#!/usr/bin/env bash
rm -rf builddocs/
sphinx-apidoc src/debug_toolbar_force --full -o docs -H 'django-debug-toolbar-force' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -V '0.1' -f -d 20
cp docs/conf.distrib docs/conf.py
