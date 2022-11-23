import json
from team_base import TeamBase
from db import dbhelper

class TeamService(TeamBase):
    # create a team
    def create_team(self, request: str) -> str:

        if len(request['name']) > 64:
            return {"error": "name cannot be more than 64 characters"}

        if len(request['description']) > 64:
            return {"error": "display_name cannot be more than 64 characters"}

        existingUser = dbhelper.get_team_by_name(request['name'])
        if existingUser != {}:
            return {"error": "Team already exists"}

        teamResponseObj = dbhelper.insert_team(request)
        return {"id": teamResponseObj['id']}

    # list all teams
    def list_teams(self) -> str:        
        return dbhelper.get_teams()

    # describe team
    def describe_team(self, request) -> str:
        team = dbhelper.get_team_by_id(request['id'])
        response = {}
        response["name"] = team["name"]        
        response["description"] = team["description"]
        response["creation_time"] = team["creation_date"]
        response["admin"] = team["admin"]

        return response

    # update team
    def update_team(self, request: str) -> str:
        print(str(request['team']))
        if len(request['team']['name']) > 64:
            return {"error": "name cannot be more than 64 characters"}

        if len(request['team']['description']) > 128:
            return {"error": "display_name cannot be more than 128 characters"}
        
        return dbhelper.update_team(request['team'], request['id'])

    # add users to team
    def add_users_to_team(self, request: str):

        users = json.dumps(request['users'])
        print(users)
        return dbhelper.add_users_team(users, request['id'])

    
    # list users of a team
    def list_team_users(self, request: str):
        users = []
        teamDetails = dbhelper.get_team_by_id(request['id'])
        
        for userid in json.loads(teamDetails['users']):
            userObj = {}            
            user = dbhelper.get_user_by_id(userid)
            print(type(user))
            userObj["id"] = int(userid)
            userObj["name"] = user["name"]
            userObj["display_name"] = user["display_name"]
            users.append(userObj)
        
        return users