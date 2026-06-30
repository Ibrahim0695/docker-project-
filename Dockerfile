FROM python:3.12-slim

WORKDIR /app

# Install build-time deps, install Python packages, then remove build deps and caches in one layer
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
