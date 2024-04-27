

FROM python:3.6

ENV PYTHONUNBUFFERED 1


RUN mkdir /ExportApi

WORKDIR /ExportApi

ADD . /ExportApi/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


