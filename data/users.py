from pathlib import Path
from model.user import User

student = User(
    first_name='Leonid',
    last_name='Chaliy',
    email='leonid@example.com',
    gender='Male',
    phone='1234567890',
    birth_day='28',
    birth_month='August',
    birth_year=2004,
    subject='Maths',
    hobby='Sports',
    picture = str(Path.cwd() / "resources" / "avatar.png"),
    address='Moscow',
    state='NCR',
    city='Delhi',
)