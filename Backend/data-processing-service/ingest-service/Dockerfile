FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8000
ENV KAFKA_BOOTSTRAP_SERVERS=
ENV KAFKA_LOCATION_DATA_TOPIC="location-data"

EXPOSE 8000

CMD ["python", "src/main.py"]