from fastapi import FastAPI
from routes.user import user_router 
from routes.event import event_router
from routes.speaker import speaker_router

app = FastAPI()
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(event_router, prefix="/event", tags=["event"])
app.include_router(speaker_router, prefix="/speaker", tags=["speaker"])

