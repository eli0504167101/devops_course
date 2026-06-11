from flask import Flask, render_template_string
import os, mysql.connector
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def get_db_config():
    return {
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME")
    }

@app.route('/')
def index():
    try:
        # שימוש ב-with סוגר את החיבור אוטומטית בסוף הבלוק
        with mysql.connector.connect(**get_db_config()) as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT name, email FROM users")
                users = cursor.fetchall()
                
                if not users: return "No users found."

                # יצירת הרשימה בשורה אחת אלגנטית
                user_list = "".join([f"<li>{u['name']} ({u['email']})</li>" for u in users])
                return f"<h1>User List</h1><ul>{user_list}</ul>"
    except Exception as e:
        return f"Connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("FLASK_PORT")), debug=True)