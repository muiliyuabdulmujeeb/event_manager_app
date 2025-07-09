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

class UserBase(UserUpdate):
    pass    
