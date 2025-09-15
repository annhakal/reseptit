import db

def add_item(title, ingredients, instructions, user_id):
    sql = """INSERT INTO items (title, ingredients, instructions, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, ingredients, instructions, user_id])

def get_items():
    sql = "SELECT id, title FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.title,
                    items.ingredients,
                    items.instructions,
                    users.username
                FROM items, users
                WHERE items.user_id = users.id AND
                items.id = ?"""
    return db.query(sql, [item_id])[0]