from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(UserCreate):
    id: str

class UserActivate(BaseModel):
    id: str

class UserDeactivate(UserActivate):
    pass

class UserBase(UserCreate, UserDeactivate):
    pass    
