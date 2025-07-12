from pydantic import BaseModel
from datetime import date

#Registration Parameters
#1. id
#2. user_id
#3. event_id
#4. registration_date
#5. attended (Default is false)

class RegistrationCreate(BaseModel):
    user_id: str
    event_id: str
    reg_date: date

class MarkAttendance(BaseModel):
    id: str
