from typing import List
from datetime import datetime

class Presentation:
    """
    Represents a presentation event.
    """
    def __init__(self, title: str, description: str, time: datetime, capacity: int, presenter: 'Presenter'):
        self.presentation_id = None
        self.title = title
        self.description = description
        self.time = time
        self.capacity = capacity
        self.presenter = presenter
        self.bookings = []
        self.location = None
        self.duration_minutes = 60
        self.status = "scheduled"  # scheduled, ongoing, completed, cancelled
        self.materials_url = None
        self.tags = []

    def add_booking(self, booking: 'Booking') -> None:
        pass

    def get_attendee_count(self) -> int:
        pass

    def get_available_slots(self) -> int:
        pass

    def is_full(self) -> bool:
        pass

    def cancel_presentation(self) -> None:
        pass