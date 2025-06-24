import reflex as rx
from typing import Optional, List

class Summary(rx.Model, table=False):
    page: int
    type: str
    content: List[str]


