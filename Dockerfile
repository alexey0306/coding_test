# Installing Python image
FROM python:3.8-slim as base

RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt

RUN pip install --prefix=/install -r /requirements.txt

# Copying compiled Python files
FROM base
COPY --from=base /install /usr/local

COPY . /srv/app
WORKDIR /srv/app
