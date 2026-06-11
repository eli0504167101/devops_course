# 1. שימוש ב-Base Image רשמי וקל משקל של פייתון
FROM python:3.10-slim

# 2. הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# 3. התקנת ה-Dependencies ישירות (בגלל שזה רק Flask, נתקין ישירות בלי קובץ requirements)
RUN pip install --no-cache-dir flask

# 4. העתקת קוד האפליקציה מהמחשב שלך לתוך הקונטיינר
COPY app.py .

# 5. חשיפת הפורט עליו רצה אפליקציית ה-Flask
EXPOSE 5000

# 6. פקודת ההרצה של האפליקציה
CMD ["python", "app.py"]