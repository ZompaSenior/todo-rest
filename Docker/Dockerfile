FROM python:3.10-alpine

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src

RUN apk update \
	&& apk add --no-cache --virtual build-deps gcc g++ python3-dev musl-dev \
	&& apk add --no-cache postgresql-dev \
	&& apk add --no-cache jpeg-dev zlib-dev \
	&& apk add --no-cache libffi-dev openssl-dev \
	&& apk add --no-cache pcre-dev

COPY requirements.txt /usr/src/app/
COPY pytest.ini /usr/src/
COPY todorest_uwsgi.ini /etc/uwsgi/tonf.d/

RUN pip install --no-cache-dir -r app/requirements.txt

RUN apk del build-deps

RUN export LC_ALL="en_US.UTF-8"
