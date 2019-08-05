FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt-get install -y gettext
COPY requirements.txt /tmp/
RUN apt-get update && apt-get -y install cmake
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/
