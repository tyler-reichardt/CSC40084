from user import User
from typing import List

class Presenter(User):
    """
    Represents a user who can create and manage presentations.
    Inherits from User.
    """
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, bio: str = ""):
        pass

    def create_presentation(self, title: str, description: str, time: str, capacity: int) -> 'Presentation':
        pass

    def view_my_presentations(self) -> List['Presentation']:
        pass