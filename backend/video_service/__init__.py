from backend.video_service.service import (
    analyze_video,
    detect_face,
    task_video_analysis,
)
from backend.video_service.model import DeepfakeModel, load_model

__all__ = [
    "analyze_video",
    "detect_face",
    "task_video_analysis",
    "DeepfakeModel",
    "load_model",
]
