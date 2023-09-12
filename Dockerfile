FROM python:3.10

RUN pip install fastapi

RUN pip install uvicorn

RUN mkdir /code

WORKDIR /code

RUN git clone https://github.com/braiso-22/CozyCave-back.git

WORKDIR /code/CozyCave-back