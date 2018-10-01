#!/bin/bash

python manage.py makemessages -l 'en'
python manage.py compilemessages
