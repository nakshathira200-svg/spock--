from celery import Celery

celery = Celery(
    "verify",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)

from backend.video_service import task_video_analysis
from backend.audio_service import task_audio_analysis
