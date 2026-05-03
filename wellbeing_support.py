"""Human, supportive copy: habits after prediction and how to find professional help."""

import streamlit as st

HABITS_LOW = [
    "Keep a **steady sleep window** most nights—even 30 minutes more consistency helps your mood.",
    "Swap one hour of passive scrolling for a **short walk** or a call with someone you trust.",
    "End study blocks with a **two-minute stretch**; your nervous system notices the down-shift.",
]

HABITS_MEDIUM = [
    "Try the **50/10 rule**: fifty minutes focused work, ten minutes completely away from the screen.",
    "Name one **tiny win** from today out loud; small acknowledgements lower background stress.",
    "If caffeine runs late, **cut back after mid-afternoon** so sleep can actually repair you.",
    "Schedule **one non-negotiable** joyful thing this week (music, sport, art—whatever feels like *you*).",
]

HABITS_HIGH = [
    "**Sleep first, then optimize**—even one extra hour for a few nights changes how heavy everything feels.",
    "Tell someone you trust: *“I’m overloaded.”* You do not have to carry the full story alone.",
    "Shrink today’s to-do to **one must-do** and one *nice-if*; permission to be human matters.",
    "Five minutes of **slow breathing** (in 4, hold 2, out 6) signals safety to your body.",
    "If panic or hopelessness shows up often, that is a signal to **reach past this app**—see below.",
]


def show_habit_coaching(label: str) -> None:
    if label == "Low":
        tips = HABITS_LOW
        intro = "You’re in a steadier zone right now—that’s worth protecting with small, kind routines."
    elif label == "High":
        tips = HABITS_HIGH
        intro = "That reading sounds intense. However the model labeled it, **your feelings are real**—these habits are gentle places to start."
    else:
        tips = HABITS_MEDIUM
        intro = "A middling reading often means your week has real pressure. These habits tend to soften the edges."

    st.markdown("#### Habits that usually help")
    st.caption(intro)
    for t in tips:
        st.markdown(f"- {t}")


def show_professional_help_card() -> None:
    st.markdown("---")
    st.markdown("#### When stress feels very heavy")
    st.markdown(
        "If things feel **overwhelming most days**, or you’re having thoughts of hurting yourself, "
        "please reach for **human** help—not an algorithm. You matter, and support exists."
    )

    st.error(
        "**If you might be in danger right now:** contact **local emergency services** immediately, "
        "or go to the nearest emergency department. You deserve safety."
    )

    city = st.text_input(
        "Optional: your **city or region** (we don’t store this—we only help you search)",
        placeholder="e.g. Delhi, Manchester, Ontario…",
        key="therapy_city_predictor",
    )

    st.markdown("**Finding a psychologist or counsellor near you**")
    q = city.strip() if city else ""
    if q:
        st.caption(f"Try a careful search such as: *licensed psychologist {q}* or *counsellor near {q}*.")
    else:
        st.caption("Try: *licensed therapist near me* or *psychologist [your city]* in your favourite search engine.")

    c1, c2 = st.columns(2)
    with c1:
        st.link_button("Psychology Today — therapist directory", "https://www.psychologytoday.com/us/therapists")
    with c2:
        st.link_button("Find A Helpline — worldwide", "https://findahelpline.com/")

    st.link_button("BACP therapist search (UK)", "https://www.bacp.co.uk/search/therapists/")

    st.info(
        "Your **school or university counselling centre** is often free or low-cost—worth a call even if you’re unsure."
    )


def show_medium_professional_nudge() -> None:
    with st.expander("If this has been going on for a while…"):
        st.markdown(
            "When stress **stays** medium for weeks, talking to a counsellor or GP is a strong move—not weakness. "
            "Use the same links in **Predictor** after a *High* result, or search *therapy near me* in your area."
        )
