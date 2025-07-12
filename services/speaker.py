from fastapi import HTTPException, status
import uuid
from database import speakers
from models import Speaker as SpeakerModel

class SpeakerInit:
    speaker1 = SpeakerModel(id=str(uuid.uuid4()), name="Rotimi", topic="How to be a senior Python Dev")
    speaker2 = SpeakerModel(id=str(uuid.uuid4()), name="Sagacity", topic="Effective backend engineering learning methods")
    speaker3 = SpeakerModel(id=str(uuid.uuid4()), name="Muiliyu", topic="Incorporating daily life into coding")

    speakers.append(speaker1)
    speakers.append(speaker2)
    speakers.append(speaker3)

    @staticmethod
    def all_speakers():
        return speakers


speaker_init = SpeakerInit()