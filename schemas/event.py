from pydantic import BaseModel
from datetime import date

## Event parameters
## 1. id
## 2. title
## 3. location
## 4. date
## 5. is_open (default has been set in models.py Event class)

class EventCreate(BaseModel):
    title: str
    location: str
    date: date

class EventUpdate(EventCreate):
    id: str

class EventSpeaker(BaseModel):
    id: str
    event_id: str
    speaker_id: str