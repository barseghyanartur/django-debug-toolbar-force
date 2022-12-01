#!/usr/bin/env bash
cd examples/requirements/

echo "pip-compile common.in"
pip-compile common.in "$@" --resolver=backtracking

echo "pip-compile debug.in"
pip-compile debug.in "$@" --resolver=backtracking

echo "pip-compile deployment.in"
pip-compile deployment.in "$@" --resolver=backtracking

echo "pip-compile deployment.in"
pip-compile dev.in "$@" --resolver=backtracking

echo "pip-compile django_2_2.in"
pip-compile django_2_2.in "$@" --resolver=backtracking

echo "pip-compile django_3_0.in"
pip-compile django_3_0.in "$@" --resolver=backtracking

echo "pip-compile django_3_1.in"
pip-compile django_3_1.in "$@" --resolver=backtracking

echo "pip-compile django_3_2.in"
pip-compile django_3_2.in "$@" --resolver=backtracking

echo "pip-compile django_4_0.in"
pip-compile django_4_0.in "$@" --resolver=backtracking

echo "pip-compile django_4_1.in"
pip-compile django_4_1.in "$@" --resolver=backtracking

echo "pip-compile docs.in"
pip-compile docs.in "$@" --resolver=backtracking

echo "pip-compile documentation.in"
pip-compile documentation.in "$@" --resolver=backtracking

echo "pip-compile code_quality.in"
pip-compile code_quality.in "$@" --resolver=backtracking

echo "pip-compile test.in"
pip-compile test.in "$@" --resolver=backtracking

echo "pip-compile testing.in"
pip-compile testing.in "$@" --resolver=backtracking
