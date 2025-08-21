from user import User
from typing import List, Optional

class Attendee(User):
    """
    Represents a user who can book and view presentations.
    Inherits from User.
    """
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str):
        super().__init__(user_id, first_name, last_name, email)
        self.bookings = []
        self.interests = []
        self.attended_presentations = []
        self.feedback_given = []

    def book_presentation(self, presentation: 'Presentation') -> Optional['Booking']:
        pass

    def view_my_bookings(self) -> List['Presentation']:
        pass