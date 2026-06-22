import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Student Performance Dashboard",
    layout="wide"
)

# ==============================
# TITLE (UPGRADED UI)
# ==============================
st.markdown(
    "<h1 style='text-align:center; color:#4CAF50;'>Student Analytics Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown("### 📊 Student Performance, Study Behavior & Risk Analysis")

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("cleaned_student_data.csv")

# ==============================
# SIDEBAR (UPGRADE 1)
# ==============================
st.sidebar.title(" About Project")
st.sidebar.info(
    "Student Performance Analytics System built using Python, Pandas, "
    "and Streamlit to analyze academic performance patterns and risk factors."
)

st.sidebar.header("Filters")

performance_filter = st.sidebar.multiselect(
    "Select Performance Level",
    df["Performance_Level"].unique(),
    df["Performance_Level"].unique()
)

df_filtered = df[df["Performance_Level"].isin(performance_filter)]

# ==============================
# KPI METRICS
# ==============================
st.subheader(" Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Average Marks", round(df["Final_Marks"].mean(), 2))
col3.metric(
    "At Risk Students",
    len(df[df["Risk_Category"] == "At Risk"])
)

st.divider()

# ==============================
# GRAPH 1: STUDY HOURS VS MARKS
# ==============================
st.subheader(" Study Hours vs Final Marks")

fig, ax = plt.subplots()
sns.scatterplot(
    data=df_filtered,
    x="Study_Hours",
    y="Final_Marks",
    ax=ax
)
st.pyplot(fig)

# ==============================
# GRAPH 2: ATTENDANCE VS MARKS
# ==============================
st.subheader(" Attendance vs Final Marks")

fig, ax = plt.subplots()
sns.scatterplot(
    data=df_filtered,
    x="Attendance",
    y="Final_Marks",
    ax=ax
)
st.pyplot(fig)

# ==============================
# GRAPH 3: PERFORMANCE DISTRIBUTION
# ==============================
st.subheader(" Performance Level Distribution")

fig, ax = plt.subplots()
sns.countplot(
    data=df,
    x="Performance_Level",
    ax=ax
)
st.pyplot(fig)

# ==============================
# HEATMAP
# ==============================
st.subheader("🔥 Correlation Heatmap")

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    ax=ax
)
st.pyplot(fig)

st.divider()

# ==============================
# DATA PREVIEW + DOWNLOAD (UPGRADE 3)
# ==============================
st.subheader(" Filtered Data Preview")

st.dataframe(df_filtered)

csv = df_filtered.to_csv(index=False)

st.download_button(
    label="⬇ Download Filtered Data",
    data=csv,
    file_name="students_filtered_data.csv",
    mime="text/csv"
)

# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.markdown("👨 Developed as part of Data Science Internship Project")