import json
from user_base import UserBase
from db import dbhelper


class userRepo(UserBase):
    dbFile = ''   
    
    def __init__(self) -> None:
        self.dbFile = 'C:\\Users\\Lenovo\\Downloads\\factwise-python\\db\\users.json'

    # list all users
    def list_users(self) -> str:
        return dbhelper.get_users()

    # create a user
    def create_user(self, request: str) -> str:
        
        if len(request['name']) > 64:
            return {"error": "name cannot be more than 64 characters"}

        if len(request['display_name']) > 64:
            return {"error": "display_name cannot be more than 64 characters"}

        existingUser = dbhelper.get_user_by_name(request['name'])
        if existingUser != {}:
            return {"error": "User already exists"}

        userResponseObj = dbhelper.insert_user(request)        
        return {"id": userResponseObj['id']}
    
    # describe user
    def describe_user(self, request: str) -> str:

        user = dbhelper.get_user_by_id(request['id'])
        response = {}
        response["name"] = user["name"]        
        response["description"] = user["description"]
        response["creation_time"] = user["creation_date"]

        return response

    # update user
    def update_user(self, request: str) -> str:

        if len(request['name']) > 64:
            return {"error": "name cannot be more than 64 characters"}

        if len(request['display_name']) > 128:
            return {"error": "display_name cannot be more than 64 characters"}
        
        return dbhelper.update_user(request['user'], request['id'])

        