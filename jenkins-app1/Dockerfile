# 1. שימוש בגרסת פייתון רשמית וקלה (Alpine Linux) כדי לשמור על Image קטן ומאובטח
FROM python:3.11-alpine

# 2. הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# 3. העתקת קובץ הדרישות תחילה (ממקסם את השימוש ב-Docker Cache לשלבי הבנייה)
COPY requirements.txt .

# 4. התקנת התלויות (Flask) ללא שמירת קבצי מטמון מיותרים
RUN pip install --no-cache-dir -r requirements.txt

# 5. העתקת שאר קבצי הקוד מהמחשב/ג'נקינס אל תוך תיקיית העבודה בקונטיינר
COPY . .

# 6. הצהרה על הפורט שהקונטיינר מאזין לו (פורט 5000 כפי שהוגדר ב-app.py)
EXPOSE 5000

# 7. הגדרת משתנה סביבה כדי למנוע מפייתון לכתוב קבצי .pyc זמניים לקונטיינר
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 8. הפקודה שתריץ את האפליקציה ברגע שהקונטיינר עולה
CMD ["python", "app.py"]# 1. שימוש בגרסת פייתון רשמית וקלה (Alpine Linux) כדי לשמור על Image קטן ומאובטח
FROM python:3.11-alpine

# 2. הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# 3. העתקת קובץ הדרישות תחילה (ממקסם את השימוש ב-Docker Cache לשלבי הבנייה)
COPY requirements.txt .

# 4. התקנת התלויות (Flask) ללא שמירת קבצי מטמון מיותרים
RUN pip install --no-cache-dir -r requirements.txt

# 5. העתקת שאר קבצי הקוד מהמחשב/ג'נקינס אל תוך תיקיית העבודה בקונטיינר
COPY . .

# 6. הצהרה על הפורט שהקונטיינר מאזין לו (פורט 5000 כפי שהוגדר ב-app.py)
EXPOSE 5000

# 7. הגדרת משתנה סביבה כדי למנוע מפייתון לכתוב קבצי .pyc זמניים לקונטיינר
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 8. הפקודה שתריץ את האפליקציה ברגע שהקונטיינר עולה
CMD ["python", "app.py"]
