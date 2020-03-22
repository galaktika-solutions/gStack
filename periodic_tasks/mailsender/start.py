#!/usr/bin/env python3
import logging
import signal
from django.conf import settings

from periodtask import Task, TaskList, SKIP
logging.basicConfig(
    format='%(message)s',
    level=logging.INFO
)


tasks = TaskList(
    Task(
        name='MailSender',
        command=('python', '/src/periodic_tasks/mailsender/run.py',),
        periods='*/10 * * * * *',
        run_on_start=settings.DEBUG,
        wait_timeout=5,
        stop_signal=signal.SIGINT,
        policy=SKIP
    )
)
tasks.start()
