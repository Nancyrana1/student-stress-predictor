import streamlit as st

from ui_theme import inject_3d_theme

st.set_page_config(
    page_title="Student Stress Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_3d_theme()

st.markdown('<span class="glow-pill">A calmer corner of the internet</span>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-3d">Hey—you made it here. Let’s breathe and figure this out together.</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="lead-warm">This little app won’t fix everything, but it can mirror how your week <em>feels</em> '
    "from your study rhythm, sleep, movement, and grades. "
    "Use the sidebar to check in with the predictor, read gentle lifestyle notes, spill your thoughts in the "
    "<strong>Mind desk</strong>, or peek under the hood in About.</p>",
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4, gap="medium")
with c1:
    st.markdown(
        '<div class="depth-card"><h3>Predictor</h3><p>Move the sliders like you’re telling a friend about an '
        "average week—then see a stress band and habits that might help.</p></div>",
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        '<div class="depth-card"><h3>Lifestyle notes</h3><p>Friendly science on sleep, balance, and movement—'
        "no guilt trips, just ideas.</p></div>",
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        '<div class="depth-card"><h3>Mind desk</h3><p>A playful spot to dump the day: messy, honest, zero judgment. '
        "Your words stay on <strong>this device</strong>.</p></div>",
        unsafe_allow_html=True,
    )
with c4:
    st.markdown(
        '<div class="depth-card"><h3>About</h3><p>How the API works and what this tool is <em>not</em> '
        "(spoiler: not a doctor).</p></div>",
        unsafe_allow_html=True,
    )

st.markdown('<hr class="soft-3d"/>', unsafe_allow_html=True)

st.subheader("Quick start")
st.markdown(
    "1. Open **Predictor** when you’re ready—no rush.\n"
    "2. Be kind with the sliders: **typical** days beat perfect ones.\n"
    "3. Read the habit ideas; if the band looks **high**, we’ll nudge you toward real-world support.\n"
    "4. Visit **Mind desk** anytime your head feels loud.\n\n"
    "**Remember:** this is an educational guess from numbers, not a diagnosis. You’re the expert on *you*."
)

with st.expander("Privacy & your words"):
    st.markdown(
        "Predictor sends numbers to your API (see **About**). **Mind desk** saves notes only in a small file "
        "on this computer (`data/journal_entries.json`)—nothing is uploaded by that page. "
        "Don’t paste passwords or secrets; treat it like a sticky note on your desk."
    )
