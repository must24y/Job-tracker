from fastapi import FastAPI

from app.api.job_application import router as job_application_router
from app.api.reminder import router as reminder_router


app = FastAPI()

app.include_router(job_application_router)
app.include_router(reminder_router)