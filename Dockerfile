FROM python:3.9-slim

RUN apt-get update && apt-get install git -y

WORKDIR /app/

ADD . /app/

ENTRYPOINT ["/app/run.sh"]
