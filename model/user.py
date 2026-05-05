from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    birth_day: str
    birth_month: str
    birth_year: int
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def birth_date(self):
        return f"{self.birth_day} {self.birth_month},{self.birth_year}"

    @property
    def picture_name(self):
        return self.picture.split("\\")[-1].split("/")[-1]