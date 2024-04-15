from typing import Annotated

from fastapi import APIRouter, Depends

from repository import CountryRepository
from schemas import CountryAdd, Country, CountryId

router = APIRouter(
    prefix="/countries",
    tags=["Countries"]
)


@router.get("")
async def get_countries() -> list[Country]:
    countries = await CountryRepository.find_all()
    return countries


@router.post("")
async def add_country(
        country: Annotated[CountryAdd, Depends()]
) -> CountryId:
    country_id = await CountryRepository.add_one(country)
    return {"ok": True, "country_id": country_id}
