import sqlite3

def connect_to_db():
    conn = sqlite3.connect('db/project_planner.db')
    return conn

def insert_user(user):
    inserted_user = {}
    conn = connect_to_db()
    try:
        
        cur = conn.cursor()
        cur.execute("""INSERT INTO users (name, display_name, creation_date)
                    VALUES (?, ?, datetime('now'))""", (user['name'],   
                    user['display_name'],) )
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_user

def get_users():
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            user = {}
            #user["id"] = i["id"]
            user["name"] = i["name"]
            user["display_name"] = i["display_name"]
            user["description"] = i["description"]
            users.append(user)

    except:
        users = []

    return users


def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = ?", 
                       (user_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["id"] = row["id"]
        user["name"] = row["name"]
        user["display_name"] = row["display_name"]
        user["description"] = row["description"]
        user["creation_date"] = row["creation_date"]
    except:
        user = {}

    return user

def get_user_by_name(name):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE name = ?", 
                       (name,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["id"] = row["id"]
        user["name"] = row["name"]
        user["display_name"] = row["display_name"]
        user["description"] = row["description"]
    except:
        user = {}

    return user

def update_user(user, id):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("""UPDATE users SET name = ?, display_name = ? WHERE id = ?""",  
                     (user["name"], user["display_name"],
                     id,))
        conn.commit()
        #return the user
        updated_user = get_user_by_id(id)

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()

    return updated_user


###team related db operations###
def get_team_by_name(name):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM teams WHERE name = ?", 
                       (name,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["id"] = row["id"]
        user["name"] = row["name"]
        user["display_name"] = row["display_name"]
        user["description"] = row["description"]
        user["creation_date"] = row["creation_date"]
    except:
        user = {}

    return user

def insert_team(team):    
    inserted_team = {}
    conn = connect_to_db()
    try:
        
        cur = conn.cursor()
        cur.execute("""INSERT INTO teams (name, description, admin, creation_date)
                    VALUES (?, ?, ?,datetime('now'))""", (team['name'],   
                    team['description'], team['admin'],) )
        conn.commit()
        inserted_team = get_team_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_team

def get_team_by_id(team_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM teams WHERE id = ?", 
                       (team_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["id"] = row["id"]
        user["name"] = row["name"]
        user["description"] = row["description"]
        user["creation_date"] = row["creation_date"]
        user["admin"] = row["admin"]
        user["users"] = row["users"]
    except:
        user = {}

    return user

def get_teams():
    teams = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM teams")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            team = {}
            #user["id"] = i["id"]
            team["name"] = i["name"]
            team["description"] = i["description"]
            team["creation_time"] = i["creation_date"]
            team["admin"] = i["admin"]
            teams.append(team)

    except:
        teams = []

    return teams

def update_team(team, id):
    updated_team = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("""UPDATE teams SET name = ?, description = ?, admin = ? WHERE id = ?""",  
                     (team["name"], team["display_name"], team["admin"],
                     id,))
        conn.commit()
        #return the user
        updated_team = get_team_by_id(id)

    except:
        conn.rollback()
        updated_team = {}
    finally:
        conn.close()

    return updated_team

def add_users_team(users, id):
    updated_team = {}    
    try:        
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("""UPDATE teams SET users = ? WHERE id = ?""",  
                     (users,
                     id,))
        conn.commit()
        #return the user
        updated_team = get_team_by_id(id)

    except:
        conn.rollback()
        updated_team = {}
    finally:
        conn.close()

    return updated_team


###project board related db operations###

def insert_board(board):
    inserted_board = {}
    conn = connect_to_db()
    try:
        
        cur = conn.cursor()
        cur.execute("""INSERT INTO boards (name, description, team_id, creation_date)
                    VALUES (?, ?, ?,datetime('now'))""", (board['name'],   
                    board['description'], board['team_id'],) )
        conn.commit()
        inserted_board = get_board_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_board

def get_board_by_id(id):
    project = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM boards WHERE id = ?", 
                       (id,))
        row = cur.fetchone()

        # convert row object to dictionary
        project["id"] = row["id"]
        project["name"] = row["name"]
        project["description"] = row["description"]
        project["status"] = row["status"]
        project["creation_date"] = row["creation_date"]
        project["team_id"] = row["team_id"]
    except:
        project = {}

    return project

def get_board_by_name(name):
    board = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM boards WHERE name = ?", 
                       (name,))
        row = cur.fetchone()

        # convert row object to dictionary
        board["id"] = row["id"]
        board["name"] = row["name"]
        board["team_id"] = row["team_id"]
        board["status"] = row["status"]
        board["description"] = row["description"]
        board["creation_date"] = row["creation_date"]
    except:
        board = {}

    return board

def update_board_status(id):
    updated_board = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("""UPDATE boards SET status = CLOSED, end_time = datetime('now') WHERE id = ?""",  
                     (id,))
        conn.commit()        
        updated_board = get_board_by_id(id)

    except:
        conn.rollback()
        updated_board = {}
    finally:
        conn.close()

    return updated_board

def get_tasks_by_project_id(id):
    tasks = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE board_id = ?", id)
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            task = {}            
            task["name"] = i["name"]
            task["description"] = i["description"]
            task["status"] = i["status"]
            task["creation_date"] = i["creation_date"]
            task["board_id"] = i["board_id"]
            task["user_id"] = i["user_id"]
            tasks.append(task)

    except:
        tasks = []

    return tasks

def insert_task(task):
    inserted_task = {}
    conn = connect_to_db()
    try:
        
        cur = conn.cursor()
        cur.execute("""INSERT INTO tasks (name, title, description, user_id, creation_date)
                    VALUES (?, ?, ?, ?,datetime('now'))""", (task['title'], task['title'],   
                    task['description'], task['user_id'],) )
        conn.commit()
        inserted_task = get_task_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_task

def get_task_by_id(id):
    task = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE id = ?", 
                       (id,))
        row = cur.fetchone()

        # convert row object to dictionary
        task["id"] = row["id"]
        task["name"] = row["name"]
        task["description"] = row["description"]
        task["status"] = row["status"]
        task["creation_date"] = row["creation_date"]
        task["user_id"] = row["user_id"]
        task["board_id"] = row["board_id"]
    except:
        task = {}

    return task

def get_task_by_title(title):
    task = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE title = ?", 
                       (title,))
        row = cur.fetchone()

        # convert row object to dictionary
        task["id"] = row["id"]
        task["name"] = row["name"]
        task["description"] = row["description"]
        task["status"] = row["status"]
        task["creation_date"] = row["creation_date"]
        task["user_id"] = row["user_id"]
        task["board_id"] = row["board_id"]
    except:
        task = {}

    return task