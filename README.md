# Countries API

A small FastAPI project that exposes a list of countries as JSON.

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
C:/Python314/python.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

Start the development server:

```powershell
python -m uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000/countries> to view the country list, or open <http://127.0.0.1:8000/docs> for the interactive API documentation.
