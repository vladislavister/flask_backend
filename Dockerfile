FROM python:3.10.7

ENV FLASK_APP=<app_name>

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY <app_folder_name> /opt/<app_folder_name>

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT
