from pydantic import BaseModel

## Speaker parameters
## 1. id
## 2. name
## 3. topic

class SpeakerCreate(BaseModel):
    name: str
    topic: str

class SpeakerUpdate(SpeakerCreate):
    id: str