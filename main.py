# gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
# uvicorn main:app --reload
from fastapi import FastAPI
from router import (
    audio_router,
    frontend_router,
)
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,  # This is required
        allow_methods=["*"],
        allow_headers=["*"],
    )
]
app = FastAPI(docs_url=None, middleware=middleware, redoc_url=None)
app.include_router(audio_router.router)
app.include_router(frontend_router.router)


@app.get("/")
def health_check():
    return "Server is up!"
