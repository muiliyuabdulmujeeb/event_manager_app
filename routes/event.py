from fastapi import APIRouter, status
from schemas.event import EventCreate, EventUpdate
from services.event import event_logic

event_router = APIRouter()

@event_router.post("/", status_code= status.HTTP_201_CREATED)
def create_event(event_details: EventCreate):
    return event_logic.create_event(event_details=event_details)

@event_router.patch("/", status_code= status.HTTP_200_OK)
def update_event(update_details: EventUpdate):
    return event_logic.update_event(update_details= update_details)

@event_router.get("/", status_code= status.HTTP_200_OK)
def get_all_events():
    return event_logic.get_all_events()

@event_router.get("/{event_id}", status_code= status.HTTP_200_OK)
def get_event_by_id(event_id: str):
    return event_logic.get_event_by_id(event_id= event_id)

@event_router.delete("/{event_id}")
def delete_event(event_id: str):
    return event_logic.delete_event(event_id= event_id)

@event_router.patch("/{event_id}/close")
def close_event_registration(event_id: str):
    return event_logic.close_event_registration(event_id= event_id)

@event_router.patch("/{event_id}/open")
def open_event_registration(event_id: str):
    return event_logic.open_event_registration(event_id= event_id)