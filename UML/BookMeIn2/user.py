class User:
    """
    Base class for all users in the BookMeIn2 system.
    """
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_logged_in = False
        self.registration_date = None

    def login(self, password: str) -> bool:
        pass

    def logout(self) -> None:
        pass

    def get_full_name(self) -> str:
        pass