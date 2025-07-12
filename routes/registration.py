from fastapi import APIRouter, status
from schemas.registration import RegistrationCreate
from services.registration import registration_logic

registration_router = APIRouter()


@registration_router.post("/register", status_code= status.HTTP_201_CREATED)
def register(reg_details: RegistrationCreate):
    return registration_logic.register_user(reg_details= reg_details)

@registration_router.patch("/{reg_id}/attend", status_code= status.HTTP_200_OK)
def mark_attendance(reg_id: str):
    return registration_logic.mark_attendance(reg_id= reg_id)

@registration_router.get("/all", status_code= status.HTTP_200_OK)
def all_registrations():
    return registration_logic.all_registrations()

@registration_router.get("/users-that-attended-at-least-one-event")
def user_attends_one_event_minimum():
    return registration_logic.user_attends_one_event_minimum()

@registration_router.get("/", status_code= status.HTTP_200_OK)
def registrations_by_user(user_id: str):
    return registration_logic.registrations_by_user(user_id= user_id)