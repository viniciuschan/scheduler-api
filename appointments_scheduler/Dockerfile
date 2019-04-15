FROM python:3.6.5

ENV PYTHONUNBUFFERED 1
RUN mkdir /appointments_scheduler/

COPY requirements.txt /appointments_scheduler/

COPY . /appointments_scheduler/

WORKDIR /appointments_scheduler/

RUN cd /appointments_scheduler && pip install -r requirements.txt
