from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History: str = 'History'
    Maths: str = 'Maths'
    Physics: str = 'Pysics'


class Hobby(Enum):
    Sports: str = 'Sports'
    Reading: str = 'Reading'
    Music: str = 'Music'


class Gender(Enum):
    Male: str = 'Male'
    Female: str = 'Female'
    Other: str = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'YouMeanIt'
    email: str = 'abc@efg.com'
    user_number: str = '1234567890'
    birth_day: str = '26'
    birth_month: str = 'May'
    birth_year: str = '1999'
    subjects: Tuple[Subject] = (Subject.History, Subject.Maths)
    current_address: str = 'The Earth'
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Reading)
    picture_file: str = 'kitten.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


student = User(name='Dan', gender=Gender.Male)
