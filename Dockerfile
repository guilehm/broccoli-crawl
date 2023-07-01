FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code

COPY poetry.lock pyproject.toml /tmp/
RUN pip install poetry
RUN cd /tmp && poetry export -f requirements.txt --output /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt