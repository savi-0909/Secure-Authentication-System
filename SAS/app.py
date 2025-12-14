from flask import Flask, request, jsonify
import sqlite3
import bcrypt
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

def get_db():
    return sqlite3.connect('database.db')

conn = get_db()
conn.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password BLOB
)
""")
conn.close()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
    conn = get_db()
    conn.execute("INSERT INTO users(username, password) VALUES (?,?)",
                 (data['username'], hashed_pw))
    conn.commit()
    conn.close()
    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE username=?",
                        (data['username'],)).fetchone()
    conn.close()

    if user and bcrypt.checkpw(data['password'].encode(), user[2]):
        token = jwt.encode({
            'user': data['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
