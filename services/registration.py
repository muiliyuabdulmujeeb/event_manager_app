from fastapi import Depends, HTTPException, status
import uuid
from schemas.registration import RegistrationCreate, MarkAttendance
from models import Registration as RegistrationModel
from database import users, events, registrations

class RegistrationLogic:

    @staticmethod
    def register_user(reg_details: RegistrationCreate):

        # check if user exists
        user_exists = False
        for user in users:
            if user.id == reg_details.user_id:
                user_exists = True
        if not user_exists:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        # check if event exists
        event_exists = False
        for event in events:
            if event.id == reg_details.event_id:
                event_exists = True
        if not event_exists:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

        #check if user is active
        user_is_active = False
        for user in users:
            if user.is_active == True:
                user_is_active = True
                break
        if not user_is_active:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not active")
        
        #check if user has previously registered for event
        user_registered = False
        for registration in registrations:
            if registration.user_id == reg_details.user_id:
                user_registered = True
                break
        if user_registered:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User has previously registered for event")
        
        #check if event is open
        event_is_open = False
        for event in events:
            if event.is_open == True:
                event_is_open = True
                break
        if not event_is_open:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Event is not open for registration")

        #When all checks are passed, handle event registration for user
        reg_id = str(uuid.uuid4())
        reg_details_data = RegistrationModel(reg_id, **reg_details.model_dump())
        registrations.append(reg_details_data)
        return reg_details_data


    @staticmethod
    def mark_attendance(reg_id: str):
        for registration in registrations:
            if registration.id == reg_id:
                registration.attended = True
                return {"Attendance Marked"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    
    @staticmethod
    def registrations_by_user(user_id: str):
        values = []
        user_present = False
        for registration in registrations:
            if registration.user_id == user_id:
                values.append(registration)
                user_present = True
        if not user_present:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return values


    @staticmethod
    def all_registrations():
        return registrations
    
    @staticmethod
    def user_attends_one_event_minimum():
        filter_list= set()
        user_present = False
        for registration in registrations:
            if registration.attended == True:
                filter_list.add(registration.user_id)
                user_present= True
        if not user_present:
            return set()
        return filter_list        

registration_logic = RegistrationLogic()