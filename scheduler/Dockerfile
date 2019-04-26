FROM python:3.6.5

ENV PYTHONUNBUFFERED 1
RUN mkdir /scheduler/

COPY requirements.txt /scheduler/

COPY . /scheduler/

WORKDIR /scheduler/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
