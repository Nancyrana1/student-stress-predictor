"""Tiny local file store for journal entries (no cloud; stays on this machine)."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

_MAX_ENTRIES = 400

_DIR = Path(__file__).resolve().parent / "data"
_FILE = _DIR / "journal_entries.json"


def _ensure_dir() -> None:
    _DIR.mkdir(parents=True, exist_ok=True)


def load_entries() -> list[dict]:
    if not _FILE.is_file():
        return []
    try:
        raw = _FILE.read_text(encoding="utf-8")
        data = json.loads(raw)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_entry(text: str) -> None:
    text = (text or "").strip()
    if not text:
        return
    _ensure_dir()
    entries = load_entries()
    entries.insert(
        0,
        {
            "ts": datetime.now().isoformat(timespec="seconds"),
            "text": text,
        },
    )
    entries = entries[:_MAX_ENTRIES]
    _FILE.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
