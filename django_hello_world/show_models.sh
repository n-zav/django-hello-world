#!/bin/bash

file_name=`date +%d-%m-%Y`
python manage.py show_models hello > $file_name.dat
