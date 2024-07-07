#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python3, but it looks like Python3 is not installed.
    To install Python3, check out https://www.python.org/downloads/' >&2
  exit 1
fi

python3 -m venv venv
source venv/bin/activate
python3 main.py

deactivate