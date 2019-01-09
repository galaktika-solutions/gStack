#!/usr/bin/env python3

import signal
import logging
import os

import django
django.setup()

from periodtask import TaskList, Task


class MainFilter():
    def filter(self, record):
        msg = record.msg
        if (
            msg.startswith('acquir') or
            msg.startswith('releas') or
            msg == '' or
            msg.startswith('-') or
            msg.startswith('done in') or
            msg.startswith('0 sent; 0 deferred') or
            msg.startswith('0 message(s) retried')
        ):
            return False
        return True


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'general': {
            'format': '|{asctime}|{message}',
            'datefmt': '%Y-%m-%d %H:%M:%S%z',
            'style': '{',
        },
    },
    'filters': {
        'main_filter': {
            '()': MainFilter,
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'general',
            'filters': ['main_filter']
        },
        'null': {
            'class': 'logging.NullHandler'
        }
    },
    'root': {
        'handlers': ['null'],
    },
    'loggers': {
        'tasklogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
})

# this is needed to handle logging properly
os.environ['NO_DEBUG_TOOLBAR'] = 'True'
tasklist = []

if os.environ.get('SEND_MAIL_TASK') == 'True':
    tasklist.append(
        Task(
            name='send_mail',
            command=('django-admin', 'send_mail'),
            periods='*/5 *',
            wait_timeout=5,
            stop_signal=signal.SIGINT,
            stderr_logger=logging.getLogger('tasklogger')
        )
    )

if os.environ.get('RETRY_DEFERRED_TASK') == 'True':
    tasklist.append(
        Task(
            name='retry_deferred',
            command=('django-admin', 'retry_deferred'),
            periods='0 */5',
            wait_timeout=5,
            stop_signal=signal.SIGINT,
            stderr_logger=logging.getLogger('tasklogger')
        )
    )

TaskList(*tasklist).start()
