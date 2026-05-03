import streamlit as st
import requests

from api_config import get_api_base, get_predict_url, get_root_url
from ui_theme import inject_3d_theme

inject_3d_theme()

st.markdown('<span class="glow-pill">Under the hood</span>', unsafe_allow_html=True)
st.title("About this project")
st.markdown(
    "There are two pieces: a **FastAPI** service that runs the saved model, and this **Streamlit** site that talks to it. "
    "Everything here is built to be kind in tone—but technically it’s still software, not a clinician."
)

st.subheader("Architecture")
st.code(
    """
You (sliders)  →  Streamlit  →  POST /predict  →  scaler + model  →  Low / Medium / High
                      ↑
                 Mind desk notes stay local on disk (data/journal_entries.json)
    """,
    language="text",
)

st.subheader("Endpoints")
st.markdown(
    f"- **Health:** `{get_root_url()}`\n"
    f"- **Predict:** `{get_predict_url()}`\n"
    "- **Docs:** add `/docs` to your API base in the browser."
)

col_a, col_b = st.columns(2)
with col_a:
    if st.button("Ping API root", use_container_width=True):
        try:
            r = requests.get(get_root_url(), timeout=30)
            if r.status_code == 200:
                st.success("API is awake.")
                st.json(r.json())
            else:
                st.warning(f"HTTP {r.status_code}")
                st.text(r.text[:500])
        except requests.RequestException as exc:
            st.error(str(exc))

with col_b:
    st.markdown(
        "**Deploying the API:** `uvicorn model:app --host 0.0.0.0 --port $PORT` with `picklefiles/` in the bundle."
    )

st.subheader("Limitations (important)")
st.markdown(
    "- Trained on **one kind of dataset**—your school, culture, or season might differ.\n"
    "- **Three buckets** miss nuance; borderline scores are fuzzy.\n"
    "- **No** trauma history, finances, family, neurodivergence—only time-use and GPA.\n"
    "- **Never** replaces therapy, meds, or emergency care.\n"
)

st.subheader("Configuration")
st.markdown(
    f"`API_BASE_URL` points Streamlit at your API (default now: `{get_api_base()}`)."
)
