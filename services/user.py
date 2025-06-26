import uuid
from database import users
from models import User as UserModel
from schemas.user import UserCreate, UserBase, UserUpdate, UserActivate, UserDeactivate

class UserLogic:
    
    @staticmethod
    def create_user(user_details: UserCreate):
       user_id = str(uuid.uuid4())
       user = UserModel(id = user_id, **user_details.model_dump())
       users.append(user)
       return user
    
    @staticmethod
    def get_user_by_id(user_id: str):
        for user in users:
            if user.id == user_id:
                return user
        return {"error": "User not found"}
    
    @staticmethod
    def get_all_users():
       return users
    
    @staticmethod
    def update_user(to_update: UserUpdate):
        for user in users:
            if user.id == to_update.id:
                user.name = to_update.name
                user.email = to_update.email
                return user
        return {"error": "User not found"}

    @staticmethod
    def deactivate_user(to_deactivate: UserDeactivate):
        for user in users:
            if user.id == to_deactivate.id:
                user.is_active = False
                return {"Message": "User deactivated"}
        return {"error": "User not found"}    

    @staticmethod
    def activate_user(to_activate: UserActivate):
        for user in users:
            if user.id == to_activate.id:
                user.is_active = True
                return {"Message": "User deactivated"}
        return {"error": "User not found"}    

    @staticmethod
    def delete_user(user_id: str):
        for user in users:
            if user.id == user_id:
                users.remove(user)
                return {"Message": "User deleted"}
        return {"error": "User not found"}
        
    

user_logic = UserLogic()