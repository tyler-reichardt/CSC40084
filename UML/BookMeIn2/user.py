class User:
    """
    Base class for all users in the BookMeIn2 system.
    """
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str):
        pass

    def login(self, password: str) -> bool:
        pass

    def logout(self) -> None:
        pass

    def get_full_name(self) -> str:
        pass