from pydantic import BaseModel

## User parameters
## 1. id
## 2. name
## 3. email
## 4. is_active (default has been set in models.py User classca)


class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(UserCreate):
    id: str

class UserActivate(BaseModel):
    id: str

class UserDeactivate(UserActivate):
    pass

class UserBase(UserCreate, UserDeactivate):  ## edit the parent class here to UserUpdate
    pass    
