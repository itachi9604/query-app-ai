FROM python:3.9-slim

WORKDIR /app

COPY ./GetQuery/requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt
