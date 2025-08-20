"""
BookMeIn2: A presentation booking system

This module provides classes for managing presentations and bookings.
"""

from .user import User
from .presenter import Presenter
from .attendee import Attendee
from .presentation import Presentation
from .booking import Booking

__all__ = ['User', 'Presenter', 'Attendee', 'Presentation', 'Booking']