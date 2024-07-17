# blog/apps.py

from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):

        from blog import scheduler
        try:
            scheduler.start()
        except Exception as e:
            logger.error(f"Failed to start scheduler: {e}")
