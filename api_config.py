import os

# Local FastAPI (run: uvicorn model:app --host 0.0.0.0 --port 8000)
# For another device on your Wi‑Fi, set API_BASE_URL=http://<this-PC-LAN-IP>:8000
_DEFAULT_BASE = "http://127.0.0.1:8000"


def get_api_base() -> str:
    return os.environ.get("API_BASE_URL", _DEFAULT_BASE).rstrip("/")


def get_predict_url() -> str:
    return f"{get_api_base()}/predict"


def get_root_url() -> str:
    return f"{get_api_base()}/"
