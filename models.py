from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Song(BaseModel):
    id: int
    title: str
    score: int
    country: str
    date_added: datetime
    date_modified: datetime

    