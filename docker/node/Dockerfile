FROM ubuntu:bionic-20181112

ENV DEBIAN_FRONTEND noninteractive

# locales
RUN apt-get update && apt-get install -y locales
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN apt-get update && apt-get install -y curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && apt-get install -y nodejs
RUN npm install -g npm@6.5.0

# python
RUN apt-get update && apt-get install -y python3.6 python3-venv
RUN python3.6 -m venv /python
ENV PATH /python/bin:$PATH
ENV PYTHONUNBUFFERED 1

# pip packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir gdockutils==0.5.16

ENV HOME /tmp
WORKDIR /src/js_client
ENV PATH $PATH:./node_modules/.bin

ENTRYPOINT ["/src/docker/node/entrypoint.sh"]
