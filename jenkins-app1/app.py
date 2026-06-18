from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    # קבלת התאריך והשעה הנוכחיים
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # האמת המקצועית: עדיף להשתמש ב-HTML בסיסי עם עיצוב קל כדי שזה ייראה טוב על המסך
    return f"""
    <html>
        <head><title>My Home and</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1>Welkome to the my home</h1>
            <p style="font-size: 1.2em; color: #555;">Current Date & Time:</p>
            <h2 style="color: #2c3e50;">{now}</h2>
        </body>
    </html>
    """

if __name__ == '__main__':
    # הרצה על פורט 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
