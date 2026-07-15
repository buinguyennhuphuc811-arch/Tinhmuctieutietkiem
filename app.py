import streamlit as st
import pandas as pd
import plotly.express as px
import math

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Savings Goal Calculator",
    page_icon="💰",
    layout="centered"
)

st.title("Savings Goal Calculator")
st.write("Calculate how long it will take to reach your savings goal.")

st.divider()

# ==========================
# User Input
# ==========================

goal = st.number_input(
    "Savings Goal (VND)",
    min_value=1,
    value=100_000_000,
    step=1_000_000
)

current = st.number_input(
    "Current Savings (VND)",
    min_value=0,
    value=20_000_000,
    step=1_000_000
)

monthly = st.number_input(
    "Monthly Savings (VND)",
    min_value=1,
    value=5_000_000,
    step=500_000
)

# ==========================
# Calculation
# ==========================

remaining = max(goal - current, 0)

if remaining == 0:
    months = 0
else:
    months = math.ceil(remaining / monthly)

years = months // 12
months_left = months % 12

progress = min(current / goal, 1.0)

# ==========================
# Results
# ==========================

st.header("Results")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Savings Goal",
        f"{goal:,.0f} VND"
    )

    st.metric(
        "Current Savings",
        f"{current:,.0f} VND"
    )

with col2:
    st.metric(
        "Remaining Amount",
        f"{remaining:,.0f} VND"
    )

    if remaining == 0:
        st.metric(
            "Time Needed",
            "Completed"
        )
    else:
        st.metric(
            "Time Needed",
            f"{years} Year(s) {months_left} Month(s)"
        )

st.divider()

# ==========================
# Progress
# ==========================

st.subheader("Progress")

st.progress(progress)

st.write(f"Progress: **{progress*100:.1f}%**")

st.divider()

# ==========================
# Pie Chart
# ==========================

chart = pd.DataFrame({
    "Category": ["Saved", "Remaining"],
    "Amount": [current, remaining]
})

fig = px.pie(
    chart,
    names="Category",
    values="Amount",
    hole=0.45,
    title="Savings Progress"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Recommendation
# ==========================

st.subheader("Recommendation")

if progress == 1:
    st.success("Congratulations! You have reached your savings goal.")

elif progress >= 0.75:
    st.success("Excellent progress. You are almost there.")

elif progress >= 0.50:
    st.info("Good progress. Keep saving consistently.")

elif progress >= 0.25:
    st.warning("You have made a good start. Try increasing your monthly savings if possible.")

else:
    st.error("Your savings have just started. Build a consistent saving habit.")

st.divider()

# ==========================
# Saving Plan
# ==========================

daily = monthly / 30
weekly = monthly / 4

st.subheader("Suggested Saving Plan")

st.write(f"Save **{daily:,.0f} VND per day**")

st.write(f"Save **{weekly:,.0f} VND per week**")

st.caption("Developed with Streamlit")
