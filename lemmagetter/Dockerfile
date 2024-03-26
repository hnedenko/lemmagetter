FROM python:3.9.5-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --user -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . /code/
CMD python3 manage.py runserver 0.0.0.0:8000