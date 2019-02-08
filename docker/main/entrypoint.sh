#!/bin/bash
set -e

################################################################################
if [ "$1" = 'clean' ]; then
  exec find . -type d -name __pycache__ -exec rm -rf {} +
fi
################################################################################
if [ "$1" = 'postgres' ]; then
  ensure_db
  exec gprun -u postgres postgres
fi
################################################################################
if [ "$1" = 'backup' ]; then
  prepare -w django
  exec backup_ui -d -f
fi
################################################################################
if [ "$1" = 'backup_task' ]; then
  exit 0
fi
################################################################################
if [ "$1" = 'restore' ]; then
  if ! [ "$ENV" = 'DEV' ]; then
    read -p "Enter hostname: " -r host
    if ! [ "$host" = "$HOST_NAME" ]; then
      echo "Hostname mismatch."; exit 1
    fi
  fi

  prepare -w django
  exec restore_ui -d -f
fi
################################################################################
if [ "$1" = 'nginx' ]; then
  prepare nginx

  if [ "$ENV" = 'DEV' ]; then
    conf=/src/conf/nginx.dev.conf
  else
    conf=/src/conf/nginx.conf
  fi
  exec nginx -c "$conf"
fi
################################################################################
# if [ "$1" = 'redis' ]; then
#   exec docker/gprun.py -u redis redis-server --bind 0.0.0.0
# fi
################################################################################
# if [ "$1" = 'daphne' ]; then
#   if [ "$ENV" = 'DEV' ]; then
#     exit 0
#   fi
#   prepare_django
#   exec docker/gprun.py -u django -s SIGINT daphne -b 0.0.0.0 -p 8001 core.asgi:application
# fi
################################################################################
if [ "$1" = 'django' ]; then
  prepare -w django
  if [ "$ENV" = 'DEV' ]; then
    exec gprun -u django -s SIGINT django-admin runserver 0.0.0.0:8000
  fi
  exec gprun -u django -s SIGINT uwsgi --ini conf/uwsgi.conf
fi
################################################################################
if [ "$1" = 'with_django' ]; then
  shift
  prepare -w django
  exec gprun -u django -s SIGINT "$@"
fi
################################################################################
if [ "$1" = 'collectstatic' ]; then
  prepare -w django
  mkdir -p static
  chown -R django:django static
  gprun -u django -s SIGINT django-admin collectstatic -c --noinput
  chown -R "$(stat -c %u:%g .git)" /src/static
  find /src/static -type d -exec chmod 755 {} +
  find /src/static -type f -exec chmod 644 {} +
  exit 0
fi
################################################################################
if [ "$1" = 'docs' ]; then
  prepare -w django
  cd docs
  mkdir -p build
  chown -R django:django build
  gprun -u django -s SIGINT sphinx-build -M html source build -E -a
  # /src/docker/gprun.py -u django make html
  # /src/docker/gprun.py -u django make latexpdf
  chown -R "$(stat -c %u:%g /src/.git)" build
  # cd /src/docs/build/latex
  # /src/docker/gprun.py -u django make all
  exit 0
fi
################################################################################
if [ "$1" = 'test' ]; then
  prepare -w django
  gprun -u django -s SIGINT coverage run django_project/manage.py test -v 2 --noinput
  coverage report
  coverage html
  chown -R "$(stat -c %u:%g /src/.git)" coverage_report
  exit 0
fi
################################################################################
if [ "$1" = 'makemigrations' ]; then
  find . -type d -name __pycache__ -exec rm -rf {} +
  chown django:django django_project/*/migrations
  prepare -w django
  # We need to do some magic to run the final chown even if makemigration
  # fails and return the correct exit code
  exitcode=0
  gprun -u django -s SIGINT django-admin makemigrations || exitcode=$?
  chown -R "$(stat -c %u:%g /src/.git)" django_project/*/migrations
  find . -type d -name __pycache__ -exec rm -rf {} +
  exit $exitcode
fi
################################################################################
# if [ "$1" = 'coverage' ]; then
#   prepare_django
#   mkdir -p /src/static
#   chown -R django:django /src/static
#   docker/gprun.py -u django coverage run --rcfile /src/.coveragerc django_project/manage.py test
#   docker/gprun.py -u django coverage html --rcfile /src/.coveragerc
#   docker/gprun.py -u django coverage report
#   chown -R "$(stat -c %u:%g .git)" /src/static
#   find /src/static -type d -exec chmod 755 {} +
#   find /src/static -type f -exec chmod 644 {} +
#   exit 0
# fi
################################################################################
if [ "$1" = 'makemessages' ]; then
  prepare -w django
  locales=$(python -c '
import django
django.setup()
from django.conf import settings
print(" ".join(["-l %s" % k for k, v in settings.LANGUAGES if k != "en"]), end="")')

  find . -type d -name __pycache__ -exec rm -rf {} +

  # allow django to write into these directories
  find django_project -type d -exec chown django:django {} +
  cd django_project
  gprun -u django -s SIGINT django-admin makemessages \
    $locales \
    --extension=html,py,tex \
    --ignore=*/migrations/* \
    -v 2
  cd /src
  # restore permissions, clean python cache
  owner="$(stat -c %u:%g .)"; find django_project -type d -exec chown "$owner" {} +

  cd js_client/src
  gprun -u django -s SIGINT django-admin makemessages --domain djangojs \
    $locales \
    -v 2
  cd /src

  find . -type d -name __pycache__ -exec rm -rf {} +
  exit 0
fi
################################################################################
# if [ "$1" = 'makemessages' ]; then
#   prepare_django
#
#   locales=$(python -c '
# import django
# from django.conf import settings
# django.setup()
# print(" ".join(["-l %s" % k for k, v in settings.LANGUAGES if k != "en"]), end="")')
#
#
#   docker/gprun.py -u django django-admin makemessages \
#     $locales \
#     --extension=html,py,tex \
#     -v 2 \
#     --ignore=*/migrations/* \
#     --ignore=*js_client/* \
#     --ignore=docs/* \
#     --ignore=static/*
#
#   docker/gprun.py -u django django-admin makemessages --domain djangojs \
#     $locales \
#     -v 2 \
#     --ignore=docs/* \
#     --ignore=js_client/build/* \
#     --ignore=*node_modules/*
#
#   exit 0
# fi
################################################################################
exec "$@"
