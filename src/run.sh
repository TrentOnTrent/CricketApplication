#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python3, but it looks like Python3 is not installed.
    To install Python3, check out https://www.python.org/downloads/' >&2
  exit 1
fi
#python3 -m env venv
source env/bin/activate
# Most likely will not be needed, maybe
# pip install -r requirements.txt

python3 main.py

deactivate