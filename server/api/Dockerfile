FROM python:3.7-alpine3.9
LABEL maintainer="@toksicon"

EXPOSE 5000

ADD server/api/requirements.txt /www/requirements.txt
ADD shared/connector/requirements.txt /www/connector/requirements.txt
WORKDIR /www

RUN apk add build-base libffi-dev openssl-dev mariadb-connector-c-dev --no-cache && \
    pip install --no-cache-dir  -r requirements.txt && \
    pip install --no-cache-dir -r /www/connector/requirements.txt && \
    apk del build-base

ADD server/api/src /www
ADD shared/connector /www/connector
ADD shared/wait-for.sh /tools/wait-for.sh
ADD shared/minio_communication.py /www/minio_communication.py
ADD shared/redis_config.py /www/redis_config.py

ENV AUTHLIB_INSECURE_TRANSPORT=true

CMD ["python", "-u", "/www/app.py"]
