"""
SpeakerStudio: Speaker portal for presentation management

This module provides classes for speakers to manage sessions, upload materials,
configure interactive settings, view analytics, and run live polls.
"""

from .session_manager import SessionManager
from .material_uploader import MaterialUploader
from .interactive_settings import InteractiveSettings
from .session_analytics import SessionAnalytics
from .live_poll_manager import LivePollManager
from .speaker_feedback import SpeakerFeedback

__all__ = [
    'SessionManager',
    'MaterialUploader',
    'InteractiveSettings',
    'SessionAnalytics',
    'LivePollManager',
    'SpeakerFeedback'
]