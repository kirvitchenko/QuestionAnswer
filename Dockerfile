FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install django djangorestframework psycopg2-binary

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]