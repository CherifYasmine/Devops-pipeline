import sqlite3
from create_db import connect_to_db, create_db_table
from utils.utils import generate_response

def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db('database.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)", (user['name'], user['email'], user['phone'], user['address'], user['country']) )
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()
    if (inserted_user != {}):
        return (generate_response(200, 'User added Successefully',inserted_user))
    else:
        return (generate_response(404, 'Could Not add User'))



def get_users():
    users = []
    try:
        conn = connect_to_db('database.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        for i in rows:
            user = {}
            user["user_id"] = i["user_id"]
            user["name"] = i["name"]
            user["email"] = i["email"]
            user["phone"] = i["phone"]
            user["address"] = i["address"]
            user["country"] = i["country"]
            users.append(user)

    except:
        users = []

    return users


def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_to_db('database.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()

        user["user_id"] = row["user_id"]
        user["name"] = row["name"]
        user["email"] = row["email"]
        user["phone"] = row["phone"]
        user["address"] = row["address"]
        user["country"] = row["country"]
    except:
        user = {}
    if user == {}:
        return (generate_response(404, 'User not found'))
    else:
        return user

def get_user_by_id2(user_id):
    user = {}
    try:
        conn = connect_to_db('database.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()

        user["user_id"] = row["user_id"]
        user["name"] = row["name"]
        user["email"] = row["email"]
        user["phone"] = row["phone"]
        user["address"] = row["address"]
        user["country"] = row["country"]
    except:
        user = {}
    return user

def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db('database.db')
        cur = conn.cursor()
        cur.execute("UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id =?", (user["name"], user["email"], user["phone"], user["address"], user["country"], user["user_id"],))
        conn.commit()
        updated_user = get_user_by_id(user["user_id"])

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()
    if user == {}:
        return (generate_response(404, 'User not found'))
    else:
        return (generate_response(200, 'User Updated Successefully',updated_user))


def delete_user(user_id):
    message = {}
    message2 = {}
    try:
        
        conn = connect_to_db('database.db')
        usr = get_user_by_id2(user_id)
        conn.execute("DELETE from users WHERE user_id = ?", (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
        message["code"] = 201
    except:
        conn.rollback()           
        print(message2)
    finally:
        conn.close()
    if (usr=={}):
        message["status"] = "Cannot delete user: user does not exist"
        message["code"] = 404    

    return message