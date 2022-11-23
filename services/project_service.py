from project_board_base import ProjectBoardBase
from db import dbhelper

class ProjectService(ProjectBoardBase):
    # create a board
    def create_board(self, request: str):

        if len(request['name']) > 64:
            return {"error": "name cannot be more than 64 characters"}

        if len(request['description']) > 128:
            return {"error": "description cannot be more than 128 characters"}

        existingBoard = dbhelper.get_board_by_name(request['name'])
        if existingBoard != {}:
            return {"error": "Board already exists"}

        userResponseObj = dbhelper.insert_board(request)        
        return {"id": userResponseObj['id']}

    # close a board
    def close_board(self, request: str) -> str:

        incompleteTasks = []
        tasks = dbhelper.get_tasks_by_project_id(request['id'])
        for task in tasks:
            if task['status'] != 'COMPLETE':
                incompleteTasks.append(task)
        
        if incompleteTasks != []:
            return {"error": "Please complete all tasks before closing the board"}

        return dbhelper.update_board_status(request['id'])

    # add task to board
    def add_task(self, request: str) -> str:

        if len(request['title']) > 64:
            return {"error": "title cannot be more than 64 characters"}

        if len(request['description']) > 128:
            return {"error": "description cannot be more than 128 characters"}

        existingBoard = dbhelper.get_task_by_title(request['title'])
        if existingBoard != {}:
            return {"error": "task with same title already exists"}

        userResponseObj = dbhelper.insert_task(request)
        return {"id": userResponseObj['id']}
    