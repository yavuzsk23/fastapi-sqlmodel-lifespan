from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)


class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs on startup: creates all tables defined by SQLModel
    SQLModel.metadata.create_all(engine)
    yield
    # Runs on shutdown: add cleanup logic here if needed


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"status": "running"}
