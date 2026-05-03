"""Shared 3D-style visuals and warm typography for Streamlit pages."""

import streamlit as st


def inject_3d_theme() -> None:
    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
        <style>
            html, body, input, button, textarea, [data-testid="stMarkdown"] {
                font-family: 'Nunito', ui-sans-serif, system-ui, sans-serif !important;
            }
            .stApp {
                background: radial-gradient(1200px 600px at 10% -10%, rgba(139, 92, 246, 0.18), transparent 55%),
                            radial-gradient(900px 500px at 95% 20%, rgba(244, 114, 182, 0.14), transparent 50%),
                            radial-gradient(800px 400px at 50% 100%, rgba(56, 189, 248, 0.08), transparent 45%),
                            linear-gradient(165deg, #0a0c14 0%, #111827 35%, #0f172a 100%) !important;
            }
            section[data-testid="stSidebar"] > div {
                background: linear-gradient(180deg, rgba(30, 41, 59, 0.92) 0%, rgba(15, 23, 42, 0.95) 100%);
                border-right: 1px solid rgba(148, 163, 184, 0.12);
            }
            .depth-card {
                transform: perspective(1100px) rotateX(2.5deg);
                transform-style: preserve-3d;
                border-radius: 20px;
                padding: 1.35rem 1.5rem;
                background: linear-gradient(155deg, rgba(51, 65, 85, 0.55) 0%, rgba(30, 41, 59, 0.75) 100%);
                border: 1px solid rgba(255, 255, 255, 0.08);
                box-shadow: 0 22px 44px -12px rgba(0, 0, 0, 0.55),
                            0 0 0 1px rgba(255, 255, 255, 0.04) inset,
                            0 -20px 40px -24px rgba(139, 92, 246, 0.35) inset;
                margin-bottom: 0.5rem;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }
            .depth-card:hover {
                transform: perspective(1100px) rotateX(1deg) translateY(-2px);
                box-shadow: 0 28px 56px -16px rgba(0, 0, 0, 0.6),
                            0 0 0 1px rgba(255, 255, 255, 0.06) inset;
            }
            .depth-card h3 {
                margin: 0 0 0.5rem 0;
                font-size: 1.08rem;
                font-weight: 800;
                letter-spacing: -0.02em;
                background: linear-gradient(90deg, #e9d5ff, #fda4af);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .depth-card p { margin: 0; line-height: 1.55; opacity: 0.92; font-size: 0.96rem; }
            h1.hero-3d {
                font-size: clamp(1.9rem, 4.2vw, 2.85rem);
                font-weight: 800;
                letter-spacing: -0.035em;
                line-height: 1.12;
                margin-bottom: 0.4rem;
                text-shadow: 0 4px 24px rgba(139, 92, 246, 0.25);
            }
            p.lead-warm {
                font-size: 1.12rem;
                line-height: 1.6;
                max-width: 44rem;
                opacity: 0.93;
            }
            .glow-pill {
                display: inline-block;
                padding: 0.35rem 0.85rem;
                border-radius: 999px;
                font-size: 0.78rem;
                font-weight: 700;
                letter-spacing: 0.04em;
                text-transform: uppercase;
                background: linear-gradient(90deg, rgba(167, 139, 250, 0.35), rgba(244, 114, 182, 0.3));
                border: 1px solid rgba(255, 255, 255, 0.12);
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
                margin-bottom: 0.75rem;
            }
            hr.soft-3d {
                border: none;
                height: 1px;
                background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.35), transparent);
                margin: 2.25rem 0;
            }
            .journal-frame {
                border-radius: 24px;
                padding: 1.5rem 1.6rem 1.25rem;
                background: linear-gradient(145deg, rgba(254, 243, 199, 0.12) 0%, rgba(253, 224, 231, 0.08) 50%, rgba(224, 231, 255, 0.1) 100%);
                border: 2px dashed rgba(251, 191, 36, 0.35);
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35),
                            inset 0 1px 0 rgba(255, 255, 255, 0.06);
                transform: perspective(1000px) rotateY(-0.5deg);
            }
            .journal-title {
                font-size: 1.45rem;
                font-weight: 800;
                margin: 0 0 0.25rem 0;
                color: #fde68a;
            }
            .journal-whisper {
                font-size: 0.95rem;
                opacity: 0.88;
                margin-bottom: 1rem;
                line-height: 1.5;
            }
            .note-bubble {
                border-radius: 16px;
                padding: 1rem 1.15rem;
                margin: 0.65rem 0;
                background: linear-gradient(135deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.9));
                border-left: 4px solid #a78bfa;
                box-shadow: 0 12px 28px rgba(0, 0, 0, 0.35);
            }
            .note-bubble small { opacity: 0.65; }
        </style>
        """,
        unsafe_allow_html=True,
    )
