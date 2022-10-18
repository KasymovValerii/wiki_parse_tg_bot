FROM python:3.9.15-slim-buster AS bot


RUN apt-get update
RUN apt-get install -y python3 python3-pip python-dev build-essential python3-venv

RUN mkdir -p /codebase
ADD . /codebase
WORKDIR /codebase

RUN pip3 install -r requirements.txt
RUN chmod +x ./codebase/bot.py

CMD python3 ./codebase/bot.py;
