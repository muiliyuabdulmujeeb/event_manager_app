from fastapi import APIRouter, status
from services.speaker import speaker_init

speaker_router = APIRouter()


@speaker_router.get("/", status_code=status.HTTP_200_OK)
def all_speakers():
    return speaker_init.all_speakers()