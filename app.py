import streamlit as st
import plotly.express as px

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Savings Goal Calculator",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Savings Goal Calculator")
st.write("Plan your savings and see how long it will take to reach your goal.")

st.divider()

# ==========================
# INPUT
# ==========================

goal = st.number_input(
    "🎯 Savings Goal (VND)",
    min_value=0,
    value=100000000,
    step=1000000
)

current = st.number_input(
    "💵 Current Savings (VND)",
    min_value=0,
    value=20000000,
    step=1000000
)

monthly = st.number_input(
    "📅 Monthly Savings (VND)",
    min_value=1,
    value=5000000,
    step=500000
)

st.divider()

# ==========================
# CALCULATION
# ==========================

remaining = max(goal - current, 0)

months = 0

if remaining > 0:
    months = remaining / monthly

years = int(months // 12)
extra_months = int(months % 12)

progress = min(current / goal, 1.0)

# ==========================
# RESULT
# ==========================

st.header("📊 Result")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Goal",
        f"{goal:,.0f} VND"
    )

    st.metric(
        "Current Savings",
        f"{current:,.0f} VND"
    )

with col2:
    st.metric(
        "Remaining",
        f"{remaining:,.0f} VND"
    )

    if remaining == 0:
        st.metric("Time Needed", "Completed 🎉")
    else:
        st.metric(
            "Time Needed",
            f"{years} years {extra_months} months"
        )

st.divider()

# ==========================
# PROGRESS BAR
# ==========================

st.subheader("📈 Progress")

st.progress(progress)

st.write(f"Progress: **{progress*100:.1f}%**")

# ==========================
# PIE CHART
# ==========================

fig = px.pie(
    names=["Saved", "Remaining"],
    values=[current, remaining],
    hole=0.45,
    title="Savings Progress"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# FINANCIAL TIPS
# ==========================

st.divider()

st.subheader("💡 Financial Tips")

if progress >= 1:
    st.success("Congratulations! You have reached your savings goal.")

elif progress >= 0.75:
    st.success("Great job! You're almost there.")

elif progress >= 0.5:
    st.info("You're halfway to your goal. Keep saving!")

elif progress >= 0.25:
    st.warning("Good start! Try increasing your monthly savings if possible.")

else:
    st.error("You're just getting started. Consistency is the key!")

# ==========================
# EXTRA INFORMATION
# ==========================

st.divider()

daily = monthly / 30

weekly = monthly / 4

st.subheader("📅 Suggested Saving Plan")

st.write(f"Save **{daily:,.0f} VND/day**")

st.write(f"Or **{weekly:,.0f} VND/week**")

st.caption("Made with ❤️ using Streamlit")
