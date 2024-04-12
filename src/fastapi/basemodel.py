from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel, Field

class Movie(BaseModel):
    mid: int
    name: str
    genre: str
    description: Optional[str] = None
    year: int
    date: Optional[datetime] = None
    rating: Union[float, int]
    actors: List[str] = []

class User(BaseModel):
    '''
    gt : greater than
    ge: greater than or equal to
    lt: less than
    le: less than or equal to
    '''
    uid: int
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=1, lt=130)

temp_movie_data = {
    'mid': 1,
    'name': 'The Dark Knight',
    'genre': 'Action',
    'description': 'A movie about Batman',
    'year': 2008,
    'date': '2021-01-01T00:00:00',
    'rating': 9.0,
    'actors': ['Christian Bale', 'Heath Ledger']
}

temp_user_data = {
    'uid': 1,
    'name': 'John',
    'age': 25
}

movie_date = Movie(**temp_movie_data)
print(movie_date)

user_data = User(**temp_user_data)
print(user_data)
