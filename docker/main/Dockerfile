FROM ubuntu:bionic-20200219

ENV DEBIAN_FRONTEND noninteractive

# locales
RUN apt-get update && apt-get install -y locales wget latexmk build-essential rsync gettext git
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# LaTex
RUN apt-get update && apt-get install -y texlive-full

# postgres
ENV PG_MAJOR 12
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999 postgres
RUN apt-get update && apt-get install -y postgresql-common
RUN sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-common/createcluster.conf
RUN apt-get update && apt-get install -y postgresql-$PG_MAJOR
ENV PATH $PATH:/usr/lib/postgresql/$PG_MAJOR/bin
ENV PGDATA /data/postgres

# python
RUN apt-get update && apt-get install -y python3.6 python3-venv python3.6-dev gcc
RUN python3.6 -m venv /python
ENV PATH /python/bin:$PATH
ENV PYTHONPATH /src/django_project/
ENV PYTHONUNBUFFERED 1

# django
RUN groupadd -r django --gid=8000 && useradd -r -m -g django --uid=8000 django
ENV DJANGO_SETTINGS_MODULE core.settings

# nginx
RUN groupadd -r nginx --gid=4430 && useradd -r -g nginx --uid=4430 nginx
RUN wget http://nginx.org/keys/nginx_signing.key
RUN apt-key add nginx_signing.key
RUN sh -c "echo 'deb http://nginx.org/packages/mainline/ubuntu/ bionic nginx' > /etc/apt/sources.list.d/Nginx.list"
RUN apt-get update && apt-get install -y nginx
RUN ln -sf /dev/stdout /var/log/nginx/access.log

# redis
RUN groupadd -r redis --gid=6379 && useradd -r -g redis --uid=6379 redis
RUN apt-get install -y redis

# pip packages
RUN pip install --no-cache-dir django==2.2.9
RUN pip install --no-cache-dir channels==2.4.0
RUN pip install --no-cache-dir channels_redis==2.4.1
RUN pip install --no-cache-dir psycopg2-binary==2.8.4
RUN pip install --no-cache-dir uwsgi==2.0.18
RUN pip install --no-cache-dir django-debug-toolbar==2.1
RUN pip install --no-cache-dir django-sql-explorer==1.1.3
RUN pip install --no-cache-dir xlsxwriter==1.2.7
RUN pip install --no-cache-dir django-extensions==2.2.5
RUN pip install --no-cache-dir coverage==5.0.1
RUN pip install --no-cache-dir periodtask==0.7.0
RUN pip install --no-cache-dir sphinx==2.3.1
RUN pip install --no-cache-dir sphinx_rtd_theme==0.4.3
RUN pip install --no-cache-dir djangorestframework==3.10.3
RUN pip install --no-cache-dir django-filter==2.2.0
RUN pip install --no-cache-dir django-rest-auth==0.9.5
RUN pip install --no-cache-dir Twisted[tls,http2]==19.10.0
RUN pip install --no-cache-dir django-rosetta==0.9.3
RUN pip install --no-cache-dir premailer==3.6.1
RUN pip install --no-cache-dir bleach==3.1.0
RUN pip install --no-cache-dir easy-thumbnails==2.7
RUN pip install --no-cache-dir django-compressor==2.3
RUN pip install --no-cache-dir django-grappelli==2.13.4
RUN pip install --no-cache-dir django-auditlog==0.4.7

# copy
COPY / /src
WORKDIR /src
RUN find /src -type d -exec chmod 777 {} +

ENTRYPOINT ["/src/docker/main/entrypoint.sh"]
