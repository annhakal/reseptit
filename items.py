import db

def add_item(title, ingredients, instructions, user_id):
    sql = """INSERT INTO items (title, ingredients, instructions, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, ingredients, instructions, user_id])