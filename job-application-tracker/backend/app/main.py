from fastapi import FastAPI

from app.api.job_application import router as job_application_router
from app.api.reminder import router as reminder_router
from app.api.auth import router as auth_router


app = FastAPI()

app.include_router(job_application_router)
app.include_router(reminder_router)
app.include_router(auth_router)