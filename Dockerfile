FROM python:3.9-alpine

WORKDIR /code

#COPY ./requirements.txt /code/requirements.txt

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./server /code/server

RUN mkdir /code/obsi

CMD ["python", "server/server.py"]

