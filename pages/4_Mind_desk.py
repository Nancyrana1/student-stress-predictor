import html
import random

import streamlit as st

from journal_storage import load_entries, save_entry
from ui_theme import inject_3d_theme

inject_3d_theme()

PROMPTS = [
    "What’s one tiny thing that actually went okay today—even 1% okay?",
    "If your brain were a roommate, what would it *not stop* talking about?",
    "What do you wish someone would say to you right now? (You can write it here.)",
    "Dump the to-do list from your head. No fixing—just listing.",
    "What scared you today, and what part of you was trying to stay safe?",
    "One sentence your future self might thank you for writing down.",
    "Something you’re proud of that you’d never post online.",
    "The thing you’re avoiding—just name it. You don’t have to solve it.",
    "Three feelings, no explanations: ______ , ______ , ______",
    "If today had a colour, what would it be—and why?",
]

STICKERS = ["✨", "🌿", "☁️", "📝", "💭", "🫧", "🌙", "🍵"]


def _next_prompt() -> None:
    st.session_state.journal_prompt = random.choice(PROMPTS)
    st.session_state.desk_sticker = random.choice(STICKERS)


if "journal_prompt" not in st.session_state:
    _next_prompt()
if "desk_sticker" not in st.session_state:
    st.session_state.desk_sticker = random.choice(STICKERS)
if "journal_widget_id" not in st.session_state:
    st.session_state.journal_widget_id = 0

if st.session_state.pop("journal_saved_flash", None):
    st.success("Saved on this device. That took courage.")
    st.balloons()

st.markdown('<span class="glow-pill">Your words, your device</span>', unsafe_allow_html=True)

sticker = st.session_state.desk_sticker
st.markdown(
    f"""
    <div class="journal-frame">
        <p class="journal-title">{sticker} Mind desk</p>
        <p class="journal-whisper">
            This isn’t homework. No grades. No “should.” Scribble nonsense, poetry, rage, or a single word.
            It’s just for you—and it stays in a little file on <strong>this computer</strong> unless you delete it.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

col_prompt, col_shuffle = st.columns([4, 1])
with col_prompt:
    st.markdown(
        f"**Today’s nudge:** *{st.session_state.journal_prompt}*",
        help="A gentle door to walk through. Ignore it if another story wants out.",
    )
with col_shuffle:
    if st.button("Surprise me ✨", use_container_width=True):
        _next_prompt()
        st.rerun()

_wid = st.session_state.journal_widget_id
_journal_key = f"journal_body_{_wid}"
st.text_area(
    "Spill it here",
    height=220,
    placeholder="Type whatever’s in your mind… typos welcome. rambling welcome. silence after typing welcome.",
    label_visibility="collapsed",
    key=_journal_key,
)

c_save, c_clear = st.columns(2)
with c_save:
    save_clicked = st.button("Save this moment 🌈", type="primary", use_container_width=True)
with c_clear:
    clear_clicked = st.button("Clear the box (doesn’t delete saved notes)", use_container_width=True)

if save_clicked:
    text = (st.session_state.get(_journal_key) or "").strip()
    if not text:
        st.warning("The box is empty—maybe you needed the quiet. Come back when words show up.")
    else:
        save_entry(text)
        st.session_state.journal_saved_flash = True
        st.session_state.journal_widget_id = _wid + 1
        st.rerun()

if clear_clicked:
    st.session_state.journal_widget_id = _wid + 1
    st.rerun()

st.divider()
st.subheader("Recent scribbles")
entries = load_entries()
if not entries:
    st.caption("Nothing here yet—your first note gets a virtual high-five when you save it.")
else:
    for entry in entries[:25]:
        ts = html.escape(entry.get("ts", ""))
        body = html.escape(entry.get("text", "")).replace("\n", "<br/>")
        st.markdown(
            f'<div class="note-bubble"><small>{ts}</small><br/>{body}</div>',
            unsafe_allow_html=True,
        )

st.caption(
    "Stored in `data/journal_entries.json` on this machine (up to 400 entries). "
    "Back it up if it matters to you."
)
