import os

# Deployed API (Render). For local dev: API_BASE_URL=http://127.0.0.1:8000
_DEFAULT_BASE = "https://student-stress-predictor-yogq.onrender.com"


def get_api_base() -> str:
    return os.environ.get("API_BASE_URL", _DEFAULT_BASE).rstrip("/")


def get_predict_url() -> str:
    return f"{get_api_base()}/predict"


def get_root_url() -> str:
    return f"{get_api_base()}/"
