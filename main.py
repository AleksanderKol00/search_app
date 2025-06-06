import logging
from contextlib import asynccontextmanager
from functools import lru_cache

import uvicorn
from fastapi import FastAPI

from config import Settings
from routes import search
from services.load_data_service import get_data_from_file


@lru_cache
def get_settings():
    return Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    loaded_data = get_data_from_file("data_files/input.txt")
    app.state.data = loaded_data
    yield


app = FastAPI(title="Search App", lifespan=lifespan)
app.include_router(search.router, prefix="/search", tags=["search"])

if __name__ == "__main__":
    log = logging.getLogger(__name__)
    logging.basicConfig(level=getattr(logging, get_settings().log_level.value, logging.INFO))

    PORT = get_settings().http_port
    log.debug(f"Starting app on PORT: {PORT}")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)
