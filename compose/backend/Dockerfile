FROM python:3.11.2-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY ../../django/requirements.txt .
RUN pip install -r requirements.txt

COPY ../../django .
