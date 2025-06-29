from fastapi import HTTPException, status
import uuid
from database import speakers
from models import Speaker as SpeakerModel
from schemas.speaker import SpeakerCreate, SpeakerUpdate

class SpeakerLogic:

    @staticmethod
    def create_speaker(speaker_details: SpeakerCreate):
        speaker_id = str(uuid.uuid4())
        speaker_data = SpeakerModel(speaker_id, **speaker_details.model_dump())
        speakers.append(speaker_data)
        return speaker_data
    
    @staticmethod
    def get_all_speakers():
        return speakers
    
    @staticmethod
    def get_speaker_by_id(speaker_id: str):
        for speaker in speakers:
            if speaker.id == speaker_id:
                return speaker
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Speaker not found")
    
    @staticmethod
    def update_speaker(speaker_details: SpeakerUpdate):
        for speaker in speakers:
            if speaker.id == speaker_details.id:
                speaker.name = speaker_details.name
                speaker.topic = speaker_details.topic
                return speaker
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Speaker not found")
    
    @staticmethod
    def delete_speaker(speaker_id: str):
        for speaker in speakers:
            if speaker.id == speaker_id:
                speakers.remove(speaker)
                return {"Message": "Speaker Deleted"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Speaker not found")




speaker_logic = SpeakerLogic()