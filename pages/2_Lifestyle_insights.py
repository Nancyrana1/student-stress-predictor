import random

import streamlit as st

from ui_theme import inject_3d_theme

inject_3d_theme()

st.markdown('<span class="glow-pill">Gentle science</span>', unsafe_allow_html=True)
st.title("Lifestyle notes")
st.markdown(
    "Think of this as a **warm pamphlet**, not a lecture. These ideas come from sleep and student-health research, "
    "but your body and culture get the final say."
)

warm_blurbs = [
    "You’re allowed to rest before you ‘earn’ it.",
    "Small steps count louder than perfect plans.",
    "Comparison steals the energy you need for healing.",
]
st.caption(random.choice(warm_blurbs))

tab_sleep, tab_balance, tab_move = st.tabs(["Sleep", "Study balance", "Movement & people"])

with tab_sleep:
    st.subheader("Sleep that actually sticks")
    st.markdown(
        "- **Roughly 7–9 hours** works for many young adults—not because of rules, but because brains clean house while you sleep.\n"
        "- **Same wake time** most days often beats obsessing over “enough” hours on paper.\n"
        "- Under **~6 hours** night after night, stress *feels* bigger even when you’re coping outwardly.\n"
    )
    st.info(
        "Try nudging sleep up **15 minutes** for a week in the Predictor and see if the band shifts—curiosity, not judgment."
    )

with tab_balance:
    st.subheader("Study without burning out")
    st.markdown(
        "- **Pomodoro-style breaks** aren’t trendy for nothing—your focus system needs off-ramps.\n"
        "- Activities you **actually like** refill you; resume-padding ones don’t count if they drain you.\n"
        "- If every hour is booked, the model isn’t wrong to worry—**white space** is a feature.\n"
    )
    st.success("Change **one slider** at a time in Predictor: you’ll learn what moves the needle for *your* week.")

with tab_move:
    st.subheader("Bodies and hearts")
    st.markdown(
        "- **Movement** can be a walk, dancing, stretching—permission to skip the gym bro aesthetic.\n"
        "- **People** who listen without fixing everything are gold; you don’t need a huge circle.\n"
        "- **GPA** here is just another input, not your value. The model doesn’t know your story.\n"
    )

st.markdown('<hr class="soft-3d"/>', unsafe_allow_html=True)
st.caption(
    "Dig deeper anytime: your campus wellness office, CDC sleep pages, or a clinician if stress won’t ease."
)
