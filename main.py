from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from database import delete_tables, create_tables
from router import router as countries_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(countries_router)
