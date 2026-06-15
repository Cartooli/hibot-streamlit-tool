"""hibot-streamlit-tool — a Study & Budget Planner.

Streamlit lets you build an interactive data app with only Python — no HTML,
no JavaScript. Two small tools here: a savings-goal calculator and a grade
averager. No API keys, no database.

Run:
    pip install -r requirements.txt
    streamlit run app.py
"""
from pathlib import Path

import streamlit as st

from logic import average, months_to_save, parse_numbers
from sanitize import clean_text

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(page_title="Hi Bot — Study & Budget Planner", page_icon="🎓")

st.title("🎓 Study & Budget Planner")
st.caption("Two quick tools. Built with Streamlit — all Python, no frontend code.")

# --- Tool 1: savings goal ---------------------------------------------------
st.header("Savings goal")
goal_name = clean_text(st.text_input("What are you saving for?", "a new laptop"))
col1, col2 = st.columns(2)
target = col1.number_input("Goal amount", min_value=0.0, value=900.0, step=50.0)
monthly = col2.number_input("Saved per month", min_value=0.0, value=75.0, step=5.0)

if monthly > 0:
    months = months_to_save(target, monthly)
    # st.write escapes goal_name by default, so typed text can't inject markup.
    st.success(f"Saving for **{goal_name or 'your goal'}**: about **{months} month(s)** to reach {target:,.0f}.")
else:
    st.info("Enter a monthly amount greater than 0 to see how long it takes.")

st.divider()

# --- Tool 2: grade average --------------------------------------------------
st.header("Grade average")
raw = st.text_input("Enter your scores, separated by commas", "90, 85, 100, 78")
scores = parse_numbers(clean_text(raw, max_len=300))
if scores:
    st.metric("Average", f"{average(scores):.1f}", help=f"From {len(scores)} score(s)")
else:
    st.info("Type some numbers, like: 90, 85, 100")

# --- Footer: about / legal --------------------------------------------------
with st.sidebar:
    st.markdown("### Hi Bot starter template")
    st.markdown("[code.hibot.space](https://code.hibot.space)")
    with st.expander("Terms of Service"):
        st.markdown((BASE_DIR / "TERMS_OF_SERVICE.md").read_text(encoding="utf-8"))
    with st.expander("Privacy Policy"):
        st.markdown((BASE_DIR / "PRIVACY_POLICY.md").read_text(encoding="utf-8"))
