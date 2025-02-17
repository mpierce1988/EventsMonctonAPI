FROM python:3.9

# Set a working directory for the current directory
WORKDIR ./

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app /app
COPY /tests /tests

CMD ["python", "./app/main.py"]