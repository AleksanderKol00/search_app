from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from routes import search
from services.load_data_service import get_data_from_file


@asynccontextmanager
async def lifespan(app: FastAPI):
    loaded_data = get_data_from_file("data_files/input.txt")
    app.state.data = loaded_data
    yield


app = FastAPI(title="Search App", lifespan=lifespan)
app.include_router(search.router, prefix="/search", tags=["search"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
