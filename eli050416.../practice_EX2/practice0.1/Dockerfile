from python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

# This Dockerfile sets up a Python 3.8 environment, copies the application code into the container, installs the required dependencies, exposes port 5000 for the application, and specifies the command to run the application when the container starts.