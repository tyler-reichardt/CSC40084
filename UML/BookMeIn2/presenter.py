from user import User
from typing import List

class Presenter(User):
    """
    Represents a user who can create and manage presentations.
    Inherits from User.
    """
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, bio: str = ""):
        super().__init__(user_id, first_name, last_name, email)
        self.bio = bio
        self.presentations = []
        self.specialization = None
        self.rating = 0.0
        self.total_presentations_given = 0

    def create_presentation(self, title: str, description: str, time: str, capacity: int) -> 'Presentation':
        pass

    def view_my_presentations(self) -> List['Presentation']:
        pass