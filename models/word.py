from typing import List

from pydantic import BaseModel


class Word(BaseModel):
    w:str
    t: List[dict] = []