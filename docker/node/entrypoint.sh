#!/bin/bash
set -e

################################################################################
if [ "$1" = 'watch' ]; then
  exec /src/docker/gprun.py -u "$(stat -c %u:%g package.json)" webpack --mode development --watch
fi
################################################################################
if [ "$1" = 'build' ]; then
  exec /src/docker/gprun.py -u "$(stat -c %u:%g package.json)" webpack --mode production
fi
################################################################################
exec "$@"
