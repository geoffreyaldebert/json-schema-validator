FROM python:3.9

COPY ./json-schema-validator /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "make", "run" ] 