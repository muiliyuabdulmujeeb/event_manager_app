from fastapi import APIRouter, status
from schemas.speaker import SpeakerCreate, SpeakerUpdate
from services.speaker import speaker_logic  

speaker_router = APIRouter()

@speaker_router.post("/", status_code= status.HTTP_201_CREATED)
def create_speaker(speaker_details: SpeakerCreate):
    return speaker_logic.create_speaker(speaker_details= speaker_details)

@speaker_router.get("/", status_code= status.HTTP_200_OK)
def get_all_speakers():
    return speaker_logic.get_all_speakers()

@speaker_router.get("/{speaker_id}", status_code= status.HTTP_200_OK)
def get_speaker_by_id(speaker_id: str):
    return speaker_logic.get_speaker_by_id(speaker_id= speaker_id)

@speaker_router.patch("/", status_code= status.HTTP_200_OK)
def update_speaker(speaker_details: SpeakerUpdate):
    return speaker_logic.update_speaker(speaker_details= speaker_details)

@speaker_router.delete("/{speaker_id}", status_code= status.HTTP_200_OK)
def delete_speaker(speaker_id: str):
    return speaker_logic.delete_speaker(speaker_id= speaker_id)