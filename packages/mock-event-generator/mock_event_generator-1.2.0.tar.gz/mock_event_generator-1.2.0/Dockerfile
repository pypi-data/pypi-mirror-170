# syntax = docker/dockerfile:1.3
ARG BUILD_ENV=dev

FROM python:3.9-slim as python-base
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --gecos '' meguser
WORKDIR /home/meguser

RUN apt-get update && apt-get --yes install gcc
RUN pip install --upgrade pip

FROM python-base as python-prod
ARG PACKAGE_VERSION
RUN --mount=type=secret,id=netrc,dst=/root/.netrc \
  pip install \
  --no-cache-dir \
  --root-user-action=ignore \
  --extra-index-url=https://git.ligo.org/api/v4/projects/11815/packages/pypi/simple \
  mock-event-generator==${PACKAGE_VERSION}

FROM python-base as python-dev
COPY pyproject.toml setup.cfg ./
COPY mock_event_generator mock_event_generator/
RUN pip install \
  --root-user-action=ignore \
  .

FROM python-${BUILD_ENV} as python-build

COPY certificate-terena-ssl-ca-3.pem .
RUN meg ca-certificate certificate-terena-ssl-ca-3.pem

USER meguser

RUN --mount=type=secret,id=x509,dst=/tmp/x509up_u1000,uid=1000 \
  meg fetch S220609hl --source playground
