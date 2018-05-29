FROM python:3.6-alpine

RUN apk update

RUN adduser -D docker
COPY --chown=docker ./app:/home/docker/packages/app
COPY --chown=docker ./tumblr_auth:/home/docker/packages/tumblr_auth
COPY --chown=docker ./docker/bin:/usr/local/bin

USER docker
RUN pip install --user docker -r requirements.txt
ENV PYTHONPATH /home/docker/packages

CMD ["cmd"]
