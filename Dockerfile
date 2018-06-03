FROM python:3.6-alpine

RUN apk update

RUN adduser -D docker
COPY --chown=docker ./requirements /home/docker/requirements
COPY --chown=docker ./packages /home/docker/packages
COPY --chown=docker ./docker/bin/cmd /usr/local/bin/cmd
RUN pip install --target="/home/docker/packages" -r /home/docker/requirements/requirements.txt

USER docker
#RUN pip install --user docker -r /home/docker/requirements/requirements.txt
ENV PYTHONPATH /home/docker/packages

CMD ["cmd"]
