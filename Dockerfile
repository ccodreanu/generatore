FROM python:3.7.6-alpine3.10

ARG version

COPY dist/generatore-$version-py3-none-any.whl .
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install ./generatore-$version-py3-none-any.whl
