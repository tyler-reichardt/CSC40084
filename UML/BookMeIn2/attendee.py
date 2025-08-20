from user import User
from typing import List, Optional

class Attendee(User):
    """
    Represents a user who can book and view presentations.
    Inherits from User.
    """
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str):
        pass

    def book_presentation(self, presentation: 'Presentation') -> Optional['Booking']:
        pass

    def view_my_bookings(self) -> List['Presentation']:
        pass