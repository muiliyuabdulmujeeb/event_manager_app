from fastapi import APIRouter, status
from schemas.user import UserCreate, UserUpdate
from services.user import user_logic

user_router = APIRouter()

@user_router.post("/", status_code= status.HTTP_201_CREATED)
def create_user(user_details: UserCreate):
   return user_logic.create_user(user_details= user_details)


@user_router.get("/all", status_code= status.HTTP_200_OK)
def get_users():
   return user_logic.get_all_users()

@user_router.get("/{user_id}", status_code= status.HTTP_200_OK)
def get_user_by_id(user_id: str):
   return user_logic.get_user_by_id(user_id= user_id)

@user_router.patch("/", status_code= status.HTTP_200_OK)
def update_user(to_update: UserUpdate):
   return user_logic.update_user(to_update=to_update)

@user_router.patch("/{user_id}/deactivate", status_code= status.HTTP_200_OK)
def deactivate_user(user_id: str):
   return user_logic.deactivate_user(user_id= user_id)

@user_router.patch("/{user_id}/activate", status_code= status.HTTP_200_OK)
def activate_user(user_id: str):
   return user_logic.activate_user(user_id= user_id)

@user_router.delete("/{user_id}", status_code= status.HTTP_200_OK)
def delete_user(user_id: str):
   return user_logic.delete_user(user_id= user_id)