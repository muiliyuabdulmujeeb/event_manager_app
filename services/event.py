from fastapi import HTTPException, status
import uuid
from database import events
from models import Event as EventModel
from schemas.event import EventCreate, EventUpdate

class EventLogic:

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

event_logic = EventLogic()