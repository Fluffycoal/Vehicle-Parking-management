# Class for Owner
class Owner:
    def __init__(self, first_name, last_name, phone_number, email):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._email = email

    def owner_info(self):
        return f"{self._first_name} {self._last_name}, Phone: {self._phone_number}, Email: {self._email}"