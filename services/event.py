from fastapi import HTTPException, status
import uuid
from database import events, speakers, event_speakers
from models import Event as EventModel
from models import EventSpeaker as EventSpeakerModel
from schemas.event import EventCreate, EventUpdate, EventSpeaker

class EventLogic:

    #event CRUD
    @staticmethod
    def create_event(event_details: EventCreate):
        event_id = str(uuid.uuid4())
        event_data = EventModel(event_id, **event_details.model_dump())
        events.append(event_data)
        return event_data
    
    @staticmethod
    def update_event(update_details: EventUpdate):
        for event in events:
            if event.id == update_details.id:
                event.title = update_details.title
                event.location = update_details.location
                event.date = update_details.date
                return event
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    
    @staticmethod
    def get_all_events():
        return events
    
    @staticmethod
    def get_event_by_id(event_id: str):
        for event in events:
            if event.id == event_id:
                return event
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    
    @staticmethod
    def delete_event(event_id: str):
        for event in events:
            if event.id == event_id:
                events.remove(event)
                return {"Message": "Event deleted"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    
    @staticmethod
    def close_event_registration(event_id: str):
        for event in events:
            if event.id == event_id:
                event.is_open = False
                return {"Message": "Event registration closed"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

    @staticmethod
    def open_event_registration(event_id: str):
        for event in events:
            if event.id == event_id:
                event.is_open = True
                return {"Message": "Event registration opened"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    
    #event_speaker CRUD
    @staticmethod
    def create_event_speaker(event_speaker_details: EventSpeaker):

        #check if speaker exists
        #global speaker_present
        speaker_present = False
        for speaker in speakers:
            if speaker.id == event_speaker_details.speaker_id:
                speaker_present = True
                break
        if not speaker_present:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Speaker does not exist, Use initialized Speaker")
        
        #check if event exists and append the event_speaker_data to event_data
        #event_present
        event_present = False
        for event in events:
            if event.id == event_speaker_details.event_id:
                event_present = True
                #handle the event speaker data
                event_speaker_id = str(uuid.uuid4())
                event_speaker_data = EventSpeakerModel(event_speaker_id, **event_speaker_details.model_dump())
                event_speakers.append(event_speaker_data)
                (event.eventspeaker).append(event_speaker_data)
                break
        if not event_present:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
        
        
        return event_speaker_data
 
    @staticmethod
    def get_all_event_speakers():
        return event_speakers
    
    @staticmethod
    def get_event_speaker_by_id(event_speaker_id: str):
        for event_speaker in event_speakers:
            if event_speaker.id == event_speaker_id:
                return event_speaker
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event speaker not found")
    
    @staticmethod
    def delete_event_speaker(event_speaker_id: str):
        #delete the event speaker in the event_speaker database
        for event_speaker in event_speakers:
            if event_speaker.id == event_speaker_id:
                event_speakers.remove(event_speaker)

         #delete the event speaker in the events database      
        for event in events:
            for speaker in event.eventspeaker:
                if speaker.id == event_speaker_id:
                    (event.eventspeaker).remove(speaker)
                    return {"Message": "Event speaker deleted"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event speaker not found")
    


event_logic = EventLogic()