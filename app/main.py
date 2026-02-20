from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.infrastructure.web.routes import router

app = FastAPI()

# Mount static files if present
app.mount('/static', StaticFiles(directory='app/infrastructure/web/static'), name='static')

# Include application routes
app.include_router(router)
