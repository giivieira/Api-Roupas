from pydantic import BaseModel
from typing import Optional


class Roupa(BaseModel):
    id: Optional[int] = None
    nome: str
    categoria: str
