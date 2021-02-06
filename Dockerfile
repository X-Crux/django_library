FROM python:3.9.1

WORKDIR /usr/src/django_library

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/django_library

CMD ["python", "manage.py", "migrate"]
