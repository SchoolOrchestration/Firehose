python manage.py migrate
gunicorn firehose.wsgi:application -b :80 --reload
