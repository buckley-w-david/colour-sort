FROM python:3.6
MAINTAINER David Buckley <buckley.w.david@gmail.com>
LABEL Description="David Buckley personal website"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .
