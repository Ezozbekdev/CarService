#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate

if [ "$POSTGRES_DB" = "carservice" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi
exec "$@"