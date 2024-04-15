from typing import Optional

from pydantic import BaseModel


class CountryAdd(BaseModel):
    name: str
    description: Optional[str] = None


class Country(CountryAdd):

    id: int


class CountryId(BaseModel):
    ok: bool = True
    country_id: int
