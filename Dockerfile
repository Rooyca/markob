FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./server /code/server

RUN mkdir /code/obsi

CMD ["uvicorn", "server.server:app", "--host", "0.0.0.0", "--port", "8888"]

