import streamlit as st
import requests

from api_config import get_api_base, get_predict_url
from ui_theme import inject_3d_theme
from wellbeing_support import (
    show_habit_coaching,
    show_medium_professional_nudge,
    show_professional_help_card,
)

inject_3d_theme()

st.markdown('<span class="glow-pill">Check-in</span>', unsafe_allow_html=True)
st.title("Predictor")
st.markdown(
    "No quiz vibes—just sliders. **Be honest**, not impressive. We’re mapping a week that already happened, "
    "not auditioning for “most productive human.”"
)
st.caption(
    f"API base: `{get_api_base()}`. "
    "For a **local** API instead, set env `API_BASE_URL=http://127.0.0.1:8000` and run "
    "`uvicorn model:app --host 127.0.0.1 --port 8000`."
)

left, right = st.columns((1.15, 1.0), gap="large")

with left:
    st.subheader("Your week, in hours")
    study = st.slider("Study hours per day", 0.0, 24.0, 6.0, 0.25, help="Classes, homework, revision combined.")
    extra = st.slider(
        "Extracurricular hours per day",
        0.0,
        24.0,
        2.0,
        0.25,
        help="Clubs, volunteering, side work—stuff that isn’t core study.",
    )
    sleep = st.slider("Sleep hours per day", 0.0, 24.0, 7.0, 0.25)
    social = st.slider("Social hours per day", 0.0, 24.0, 3.0, 0.25)
    physical = st.slider("Physical activity hours per day", 0.0, 24.0, 1.0, 0.25)
    gpa = st.slider("GPA", 0.0, 4.0, 3.5, 0.05)

    total = study + extra + sleep + social + physical
    if total > 24:
        st.warning(
            f"These add up to **{total:.1f} h/day**—more than a day holds. That’s a sign the model might be confused; "
            "tweak so it feels like a real average."
        )

with right:
    st.subheader("At a glance")
    st.metric("Rough waking hours", f"{24 - sleep:.1f} h", help="Everything except sleep, very roughly.")
    payload = {
        "Study_Hours_Per_Day": study,
        "Extracurricular_Hours_Per_Day": extra,
        "Sleep_Hours_Per_Day": sleep,
        "Social_Hours_Per_Day": social,
        "Physical_Activity_Hours_Per_Day": physical,
        "GPA": gpa,
    }
    with st.container():
        st.json(payload, expanded=False)

run = st.button("Run prediction", type="primary", use_container_width=True)

if run:
    url = get_predict_url()
    try:
        with st.spinner("Asking the model—hang tight…"):
            response = requests.post(url, json=payload, timeout=60)
    except requests.RequestException as exc:
        msg = str(exc)
        refused = (
            "10061" in msg
            or "actively refused" in msg.lower()
            or "connection refused" in msg.lower()
            or "failed to establish" in msg.lower()
        )
        if refused:
            st.error("**The prediction API is not running** (nothing is listening on that address yet).")
            with st.expander("Start the API on Windows — step by step", expanded=True):
                st.markdown(
                    f"Streamlit is calling **`{get_predict_url()}`**. That only works after you start FastAPI.\n\n"
                    "1. Open a **second** terminal (leave Streamlit running).\n"
                    "2. Go to your project folder, for example:\n"
                    "`cd C:\\Users\\Nancy\\OneDrive\\Desktop\\mera_fast_api_with_model`\n"
                    "3. Activate your venv if you use one, then run **either**:\n"
                    "```\n"
                    "python -m uvicorn model:app --host 127.0.0.1 --port 8000\n"
                    "```\n"
                    "or\n"
                    "```\n"
                    "uvicorn model:app --host 127.0.0.1 --port 8000\n"
                    "```\n"
                    "4. Wait until you see `Uvicorn running on http://127.0.0.1:8000`.\n"
                    "5. Come back here and click **Run prediction** again.\n\n"
                    "**Check:** open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in a browser—if it loads, the API is up."
                )
        else:
            st.error(f"Network problem: {exc}")
    else:
        if response.status_code == 200:
            result = response.json()
            label = result.get("stress_level_label", "Unknown")
            code = result.get("stress_level_code")

            st.divider()
            st.subheader("Here’s what came back")
            st.caption("One lens on your inputs—not the final word on your life.")

            if label == "Low":
                st.success(f"**Stress band:** {label} — looks relatively manageable from these numbers.")
            elif label == "Medium":
                st.warning(f"**Stress band:** {label} — plenty of people land here when life is full.")
            elif label == "High":
                st.error(
                    f"**Stress band:** {label} — that can be a lot to hold. "
                    "The habits below matter; if you’ve felt this way for a while, humans help more than sliders."
                )
            else:
                st.info(f"**Stress band:** {label}")

            if code is not None:
                st.caption(f"(Model code `{code}` — 0 Low, 1 Medium, 2 High)")

            show_habit_coaching(label)

            if label == "High":
                show_professional_help_card()
            elif label == "Medium":
                show_medium_professional_nudge()

            st.markdown(
                "If something **doesn’t fit** how you feel, trust yourself—and maybe jot it in **Mind desk**."
            )
        else:
            st.error(f"Request failed with HTTP **{response.status_code}**.")
            detail = response.text[:800] if response.text else "(empty body)"
            st.code(detail)
