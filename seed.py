import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM items")
db.execute("DELETE FROM item_classes")
db.execute("DELETE FROM comments")
db.execute("DELETE FROM images")

user_count = 1000
item_count = 10**6
comment_count = 10**7

for i in range(1, user_count + 1):
    sql = """INSERT INTO users (username, password_hash)
             VALUES (?, ?)"""
    db.execute(sql, ["user" + str(i), "x"])

for i in range(1, item_count + 1):
    user_id = random.randint(1, user_count)
    sql = """INSERT INTO items (title, ingredients, instructions, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, ["item" + str(i), "pepper", "mix", user_id])

for i in range(1, comment_count + 1):
    user_id = random.randint(1, user_count)
    item_id = random.randint(1, item_count)
    sql = """INSERT INTO comments (item_id, user_id, content)
             VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, "message" + str(i)])

db.commit()
db.close()

