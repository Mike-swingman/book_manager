from enum import StrEnum
from uuid import uuid4


class BookStatus(StrEnum):
    available = 'в наличии'
    booked = 'выдана'


class Book:
    def __init__(self, title: str, author: str, year: int, status: BookStatus = BookStatus.available, id: str = None):
        self.id = id or str(uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    def __str__(self) -> str:
        return f"""
        ID: {self.id}
        Title: {self.title}
        Author: {self.author}
        Year: {self.year}
        Status: {self.status}
        """
