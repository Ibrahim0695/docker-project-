# Crypto ETL (Docker Project)

This project is a small ETL pipeline that fetches cryptocurrency ticker data from CoinPaprika, transforms it into a pandas DataFrame, and loads the result into PostgreSQL.

## Structure

- `extract.py` — fetches data from the CoinPaprika API
- `transform.py` — formats and transforms the API data into a DataFrame
- `load.py` — writes the DataFrame to PostgreSQL
- `main.py` — orchestrates the ETL flow: extract → transform → load

## Requirements

- Python 3.12
- See `requirements.txt` for Python dependencies

## Run locally

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with database credentials, or set the following environment variables:

```bash
DATABASE_NAME=coinsdb
DATABASE_USER=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

4. Run the pipeline:

```bash
python main.py
```

## Run with Docker Compose (recommended)

1. Copy the example env file:

```bash
cp .env.example .env
```

2. Update `.env` with your database credentials if needed.

3. Start the services:

```bash
docker compose up --build
```

or if your system uses the legacy binary:

```bash
docker-compose up --build
```

The `docker-compose.yml` starts two services:

- `db` — Postgres database
- `app` — the Python ETL service

The app reads DB connection settings from `.env` and connects to the `db` service.

## Notes

- `main.py` is the entrypoint for the ETL pipeline.
- If you update `load.py` or other source files, rebuild the Docker image before rerunning the app.
- If the container fails immediately, check Docker logs with `docker compose logs app` or `docker-compose logs app`.
