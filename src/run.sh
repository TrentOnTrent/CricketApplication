#!/bin/bash
python3 -m env venv
source ../env/bin/activate
# Most likely will not be needed, maybe
#pip install -r requirements.txt

python3 main.py

deactivate