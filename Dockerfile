FROM python:3.9-slim

WORKDIR /app/

ADD . /app/

RUN touch apilib/__init__.py ; \
	pip3 install -q -r apilib/requirements.txt

ENTRYPOINT ["python3", "main.py"]
