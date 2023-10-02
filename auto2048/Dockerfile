FROM python:3.11

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR "/usr/src/app"
STOPSIGNAL SIGINT

ADD . /usr/src/app

RUN pip install -r requirements.txt

CMD python main.py
