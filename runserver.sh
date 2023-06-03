#!/bin/bash
sed -i -e "s/to_edit/$1/g" QRMenu/settings.py
python manage.py runserver 0.0.0.0:8000