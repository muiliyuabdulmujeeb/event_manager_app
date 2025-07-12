from pydantic import BaseModel, PrivateAttr
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
    _event_speaker: list[str] = PrivateAttr(default_factory=list)

class EventUpdate(EventCreate):
    id: str

class EventSpeaker(BaseModel):
    event_id: str
    speaker_id: str

## how about i create eventspeaker service as a separate entity and but if i want to use eventspeaker, there has to be eventid and it hasn't been created first. I will only have an eventid when i create an event  but i want the eventspeaker details to be part of what i would return when an event is successfully created.