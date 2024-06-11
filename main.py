from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from routes import putJob
from adapter.domain import database
from adapter.domain.database  import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=database.engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(putJob.router)