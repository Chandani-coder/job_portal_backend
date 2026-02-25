from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, jobs, applications

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Portal API")

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(applications.router)
