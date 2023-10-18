FROM python:3.11-bookworm
LABEL authors="mazali"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "main.py"]



ENTRYPOINT ["top", "-b"]