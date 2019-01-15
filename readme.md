# Galaktika Solutions - Software Stack

- PIP [![Requirements Status](https://requires.io/github/galaktika-solutions/gStack/requirements.svg?branch=master)](https://requires.io/github/galaktika-solutions/gStack/requirements/?branch=master)
- NodeJS [![dependencies Status](https://david-dm.org/galaktika-solutions/gStack/status.svg?path=js_client)](https://david-dm.org/galaktika-solutions/gStack?path=js_client)
- Python 3.6
- Postgres 10 [latest]
- Nginx [latest]

# `.env`

```env
COMPOSE_FILE=docker-compose.yml:docker-compose.dev.yml
ENV=DEV
# ENV=PROD
LOG_DRIVER=json-file
COMPOSE_PROJECT_NAME=gstack
REGISTRY_URL=gstack
VERSION=latest

HOST_NAME=gstack.localhost
SERVER_IP=127.0.0.1
BACKUP_UID=1000

MAIL_ADMINS_ON_ERROR_IN_DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_TIMEOUT=10
SERVER_EMAIL=...
DEFAULT_FROM_EMAIL=...
ADMINS=name1 <email1>, name2 <email2>
REWRITE_RECIPIENTS=...

SEND_MAIL_TASK=True
RETRY_DEFERRED_TASK=True
```

# `.secret.env`

```env
DB_PASSWORD_DJANGO=
DB_PASSWORD_EXPLORER=
DB_PASSWORD_POSTGRES=
DJANGO_SECRET_KEY=
PG_CLIENT_SSL_CACERT=
PG_CLIENT_SSL_CERT=
PG_CLIENT_SSL_KEY=
PG_SERVER_SSL_CACERT=
PG_SERVER_SSL_CERT=
PG_SERVER_SSL_KEY=
SITE_SSL_CERT=
SITE_SSL_KEY=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

## Populate secrets for development

After cloning, create `.env` and `.secret.env` files.

```
make createcerts
make migrate
make createsecret
```

Use the `ca.crt` for `PG_CLIENT_SSL_CACERT`, `PG_SERVER_SSL_CACERT`,
`.crt` for `PG_CLIENT_SSL_CERT`, `PG_SERVER_SSL_CERT`, `SITE_SSL_CERT`,
`.key` for `PG_CLIENT_SSL_KEY`, `PG_SERVER_SSL_KEY`, `SITE_SSL_KEY`.

Also install the `ca.crt` in your browser. If you keep the `HOST_NAME`
variable as is (`gstack.localhost`), the `hosts` file does not need to be
adjusted.

The passwords can be random strings. `EMAIL_HOST_USER` and
`EMAIL_HOST_PASSWORD` can be set in the terminal (`createsecret` option).
The example setup uses gmail, it will only work if you enable
"less secure apps" in gmail settings.

```
make migrate
make createsuperuser
```
