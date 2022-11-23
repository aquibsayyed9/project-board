import sqlite3

file = "db/project_planner.db"
try:
  conn = sqlite3.connect(file)
  print("Database formed.")  
except:
  print("err: Database not formed.")

c = conn.cursor()

# c.execute("""CREATE TABLE users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     display_name TEXT,
#     description TEXT,
#     creation_date TEXT,
#     update_date TEXT
# )""")

# c.execute("""CREATE TABLE teams(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     admin INTEGER,
#     name TEXT,
#     description TEXT,
#     users TEXT,
#     creation_date TEXT,
#     update_date TEXT
# )""")

# c.execute("""CREATE TABLE boards(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,    
#     name TEXT,
#     description TEXT,
#     team_id INTEGER,
#     title TEXT,
#     status TEXT,
#     end_time TEXT,
#     creation_date TEXT,
#     update_date TEXT
# )""")

c.execute("""CREATE TABLE tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    name TEXT,
    description TEXT,
    user_id INTEGER,
    board_id INTEGER,
    title TEXT,
    status TEXT,
    creation_date TEXT,
    update_date TEXT
)""")

# c.execute("""DROP TABLE users""")
# c.execute("""DROP TABLE teams""")
# c.execute("""DROP TABLE boards""")
# c.execute("""DROP TABLE tasks""")
conn.commit()

conn.close()