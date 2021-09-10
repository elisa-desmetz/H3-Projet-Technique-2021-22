#!/bin/bash

echo "Waiting for MySql..."
while  ! nc -z db 3306
do
    sleep 0.1
done

echo "Mysql Started"

#python ./main.py

uvicorn main:app --host 0.0.0.0 --port 80