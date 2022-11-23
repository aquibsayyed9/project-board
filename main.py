import json
from services import userRepository, teamService, project_service

from flask import Flask, request, jsonify

from services.project_service import ProjectService

app = Flask(__name__)


##user related endpoints
@app.route('/api/users/list',  methods = ['GET'])
def getUsers():
    userRepoObj = userRepository.userRepo()
    return jsonify(userRepoObj.list_users())

@app.route('/api/users/create',  methods = ['POST'])
def createUser():    
    userRepoObj = userRepository.userRepo()
    user = request.get_json()
    # print("received request: " + str(user))
    return jsonify(userRepoObj.create_user(user))

@app.route('/api/users/userDescription',  methods = ['POST'])
def getUserDescription():
    userRepoObj = userRepository.userRepo()    
    return jsonify(userRepoObj.describe_user(request.get_json()))

@app.route('/api/users/update',  methods = ['POST'])
def updateUser():
    userRepoObj = userRepository.userRepo()    
    return jsonify(userRepoObj.update_user(request.get_json()))


##team related endpoints
@app.route('/api/teams/create',  methods = ['POST'])
def createTeam():    
    teamObj = teamService.TeamService()
    team = request.get_json()
    return jsonify(teamObj.create_team(team))

@app.route('/api/teams/list',  methods = ['GET'])
def getTeams():
    teamObj = teamService.TeamService()
    return jsonify(teamObj.list_teams())

@app.route('/api/teams/teamDescription',  methods = ['POST'])
def getTeamDescription():
    teamObj = teamService.TeamService()
    return jsonify(teamObj.describe_team(request.get_json()))

@app.route('/api/teams/update',  methods = ['POST'])
def updateTeam():
    teamObj = teamService.TeamService()   
    return jsonify(teamObj.update_team(request.get_json()))

@app.route('/api/teams/addusers',  methods = ['POST'])
def addUsersToTeam():
    teamObj = teamService.TeamService()   
    return jsonify(teamObj.add_users_to_team(request.get_json()))

@app.route('/api/teams/listusers',  methods = ['POST'])
def getTeamUsers():
    teamObj = teamService.TeamService()
    return jsonify(teamObj.list_team_users(request.get_json()))


##project related endpoints
@app.route('/api/boards/create',  methods = ['POST'])
def createTeam():    
    boardObj = project_service.ProjectService()
    board = request.get_json()
    return jsonify(boardObj.create_team(board))

@app.route('/api/boards/addTask',  methods = ['POST'])
def createTeam():    
    boardObj = project_service.ProjectService()
    task = request.get_json()
    return jsonify(boardObj.add_task(task))

@app.route('/api/boards/close',  methods = ['POST'])
def closeBoard():    
    boardObj = project_service.ProjectService()
    board = request.get_json()
    return jsonify(boardObj.close_board(board))


app.run()
    