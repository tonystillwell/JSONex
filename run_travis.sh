#!/usr/bin/env bash
python JSONex.py > /dev/null &
nosetests --with-coverage
