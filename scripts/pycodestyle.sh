#!/usr/bin/env bash
reset
pycodestyle src/debug_toolbar_force/ --exclude migrations,south_migrations
