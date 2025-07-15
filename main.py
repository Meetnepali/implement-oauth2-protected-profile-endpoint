from fastapi import FastAPI
from api.v1 import articles

app = FastAPI()
app.include_router(articles.router)
