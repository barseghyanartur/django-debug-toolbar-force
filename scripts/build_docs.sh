#!/usr/bin/env bash
./scripts/uninstall.sh
./scripts/install.sh
sphinx-build -n -a -b html docs builddocs
cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..
