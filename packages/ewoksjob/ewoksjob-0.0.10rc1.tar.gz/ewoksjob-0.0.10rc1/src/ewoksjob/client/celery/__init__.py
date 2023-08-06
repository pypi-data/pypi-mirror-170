"""Remote worker pool managed by Celery
"""
import os
from celery.exceptions import TaskRevokedError as CancelledError  # noqa F401
from .tasks import *  # noqa F403
from .utils import *  # noqa F403
from .tasks import trigger_workflow as submit  # noqa F401
from .tasks import trigger_test_workflow as submit_test  # noqa F401

os.environ.setdefault("CELERY_LOADER", "ewoksjob.config.EwoksLoader")
