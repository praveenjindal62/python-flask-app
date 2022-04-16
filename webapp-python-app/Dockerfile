FROM alpine 
COPY code/requirements.txt /tmp
RUN apk add --no-cache python3 py3-pip && pip install -r /tmp/requirements.txt && mkdir -p /opt/app
WORKDIR /opt/app
COPY code .
ENTRYPOINT ["startup.sh"]