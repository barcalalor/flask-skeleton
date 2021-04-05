FROM python:3.8

WORKDIR /opt/app

RUN mkdir -p app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
