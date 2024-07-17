# blog/scheduler.py
import warnings

from backports.zoneinfo import ZoneInfo
from future.backports.datetime import datetime
from pytz_deprecation_shim import timezone

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging

warnings.filterwarnings('ignore', category=UserWarning, module='apscheduler')
logger = logging.getLogger(__name__)


def my_scheduled_task():
    # 你的任务逻辑
    logger.info("Scheduled task running now")


def start():
    tz = ZoneInfo("Asia/Shanghai")
    scheduler = BackgroundScheduler(timezone=tz)  # 设置时区为UTC
    trigger = CronTrigger(hour=13, minute=56, timezone=tz)  # 每天18:00 运行

    scheduler.add_job(my_scheduled_task, trigger)
    scheduler.start()
    logger.info("Scheduler started and job added.")
