FROM python:3.10.8

EXPOSE 8000

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver