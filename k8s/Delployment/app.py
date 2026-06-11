from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "my dream is come true"

if __name__ == '__main__':
    # הרצת השרת במצב בדיקה (Debug) על פורט 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
