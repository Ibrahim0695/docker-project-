# Crypto ETL

A Python ETL pipeline that fetches cryptocurrency ticker data from CoinPaprika, transforms the first five results, and loads them into PostgreSQL.

## Project files

- `extract.py` fetches ticker data from CoinPaprika.
- `transform.py` selects and formats the coin fields.
- `load.py` writes the results to the PostgreSQL `coins` table.
- `main.py` runs the extract → transform → load pipeline.
- `docker-compose.yml` defines the PostgreSQL database and ETL app services.

## Requirements

- Python 3.12
- PostgreSQL, or Docker Desktop with Docker Compose
- Internet access to reach CoinPaprika

## Run locally on Windows

Create and activate a Windows virtual environment, then install the dependencies:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Configure the `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST`, and `DATABASE_PORT` environment variables for a reachable PostgreSQL database. Keep database credentials private and out of source control.

Run the pipeline:

```powershell
python main.py
```

In VS Code, select `.venv\Scripts\python.exe` as the workspace interpreter. The workspace settings are configured to use this environment and activate it in new terminals.

## Run with Docker Compose

Provide the PostgreSQL settings to both services using a private local environment configuration. The `db` service needs the standard PostgreSQL settings; the `app` service needs `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST` (set to `db`), and `DATABASE_PORT`. Do not put credentials in this README or commit them to source control.

Start the services:

```powershell
docker compose up --build
```

The app runs the pipeline when it starts. To stop the services, press `Ctrl+C`; to remove the containers while keeping the database volume, run:

```powershell
docker compose down
```

## Data behavior

Each run loads the first five CoinPaprika ticker results into the PostgreSQL `coins` table. The loader uses `if_exists="replace"`, so it replaces the table and its contents on every successful run.
