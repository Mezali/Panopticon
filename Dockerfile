FROM python:3.11-slim

LABEL maintainer="Mazali"
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "80"]