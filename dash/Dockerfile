FROM python:3.10-slim-buster

WORKDIR /usr/src/dash

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]