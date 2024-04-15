from pydantic import ConfigDict
from sqlalchemy import select

from database import new_session, CountryOrm
from schemas import CountryAdd, Country


class CountryRepository:
    @classmethod
    async def add_one(cls, data: CountryAdd):
        async with new_session() as session:
            country_dict = data.model_dump()

            country = CountryOrm(**country_dict)
            session.add(country)
            await session.flush()
            await session.commit()
            return country.id

    @classmethod
    async def find_all(cls) -> list[Country]:
        async with new_session() as session:
            query = select(CountryOrm)
            result = await session.execute(query)
            country_models = result.scalars().all()
            country_schemas = [Country.model_validate(country_model.__dict__) for country_model in country_models]
            return country_schemas
