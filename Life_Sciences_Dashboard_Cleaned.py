# ============================================================
# Life Sciences Research Intelligence Dashboard
# Domain: Biomarker Analytics
# Developed By: Ananya Kapoor
# ============================================================
# PSEUDOCODE
# START

# 1. IMPORT LIBRARIES
#     Import Streamlit library
#     Import Pandas library

# 2. CONFIGURE APPLICATION
#     Set page title
#     Set page icon
#     Set page layout as wide

# 3. APPLY CUSTOM STYLING
#     Define CSS styling
#     Apply background formatting
#     Apply metric card formatting

# 4. LOAD DATASET
#     Read biomarker_dataset.csv

#     IF dataset file exists THEN

#         Load data into DataFrame

#     ELSE

#         Display error message
#         Stop application execution

#     END IF

# 5. CREATE SIDEBAR NAVIGATION
#     Create menu options:

#         • Home
#         • View Data
#         • Search Data
#         • Filter Data
#         • Metrics Dashboard
#         • Insights Dashboard
#         • Health Score

# 6. HOME PAGE
#     Display dashboard title

#     Calculate:

#         Total Records
#         Total Fields
#         Total Diseases
#         Total Researchers

#     Display summary metrics

#     Display dataset information

# 7. VIEW DATA PAGE
#     Display complete dataset
#     Provide dataset download option
# 8. SEARCH DATA PAGE
#     Accept search keyword from user
#     Search keyword in:
#         Biomarker_Name
#         Disease
#         Researcher_Name
#     IF matching records exist THEN
#         Display matching records
#     ELSE
#         Display no records found message
#     END IF
# 9. FILTER DATA PAGE
#     Create filter controls for:
#         Validation Status
#         Country
#         Priority
#     Apply selected filters
#     Generate filtered dataset
#     Display filtered records
#     Display total filtered record count
# 10. METRICS DASHBOARD
#     Calculate:
#         Total Biomarkers
#         Total Validated Biomarkers
#         Total Pending Biomarkers
#         Total High Priority Biomarkers
#         Total Sample Count
#     Display KPI metrics
#     Generate Validation Status Distribution
#     Display chart
# 11. INSIGHTS DASHBOARD
#     Determine:
#         Most Studied Disease
#         Most Active Researcher
#         Top Country
#         Highest Expression Biomarker
#         Highest Sample Count Biomarker
#     Display analytical insights
#     Generate Disease Distribution
#     Display chart
# 12. HEALTH SCORE MODULE
#     Create Health Score Formula
#         Health Score =
#         (Expression Level × 0.6)
#         +
#         ((Sample Count ÷ 10) × 0.4)
#     FOR each biomarker
#         Calculate Health Score
#         IF score ≥ 70 THEN
#             Assign "High"
#         ELSE IF score ≥ 40 THEN
#             Assign "Medium"
#         ELSE
#             Assign "Low"
#         END IF
#     END FOR
#     Sort biomarkers by Health Score
#     Display ranked table
#     Identify top biomarker
#     Display highest Health Score
#     Generate Score Distribution
#     Display chart
# 13. END APPLICATION
#     Dashboard execution completed
# END
# cd C:\Users\ananya.kapoor\Desktop\Python_task_5
# dir
# python -m streamlit run Life_Sciences_Dashboard_Cleaned.py

# ============================================================
#Import Libraries
import streamlit as st
import pandas as pd
# ============================================================

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="🧬 Life Sciences Research Intelligence Dashboard",
    page_icon="🧬",
    layout="wide"
)

# Page header
st.write("Biomarker Analytics Platform | Excelra Research Intelligence Solution")

# ============================================================
# Minimal Styling
# ============================================================
st.markdown("""
<style>

.stApp {
    background-color: #0F172A;
}

h1, h2, h3, p, label {
    color: white !important;
}

[data-testid="stMetric"] {
    background-color: #1E3A8A;
    border-radius: 10px;
    padding: 10px;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricValue"] {
    color: white !important;
}

section[data-testid="stSidebar"] {
    background-color: #172554;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# Load Dataset
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("biomarker_dataset.csv")

df = load_data()

# ============================================================
# Sidebar Navigation
# ============================================================

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "View Data",
        "Search Data",
        "Filter Data",
        "Metrics Dashboard",
        "Insights Dashboard",
        "Health Score"
    ]
)

# ============================================================
# Dashboard Header
# ============================================================

st.title("🧬 Life Sciences Research Intelligence Dashboard")
st.write("Biomarker Analytics Platform")

# ============================================================
# TASK 1 - HOME
# ============================================================

if menu == "Home":
    st.header("Welcome")
    st.write("Explore biomarker research data using search, filters, metrics, and insights.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Records", len(df))
    c2.metric("Fields", len(df.columns))
    c3.metric("Diseases", df["Disease"].nunique())
    c4.metric("Researchers", df["Researcher_Name"].nunique())

# ============================================================
# TASK 1 - VIEW DATA
# ============================================================

elif menu == "View Data":
    st.header("Dataset")
    st.dataframe(df, use_container_width=True)

# ============================================================
# TASK 3 - SEARCH FUNCTIONALITY
# ============================================================

elif menu == "Search Data":

    st.header("Search Records")

    search_term = st.text_input(
        "Enter Biomarker, Disease or Researcher"
    )

    if search_term:

        mask = (
            df["Biomarker_Name"].str.contains(search_term, case=False, na=False) |
            df["Disease"].str.contains(search_term, case=False, na=False) |
            df["Researcher_Name"].str.contains(search_term, case=False, na=False)
        )

        results = df[mask]

        st.write(f"Matching Records: {len(results)}")
        st.dataframe(results, use_container_width=True)

# ============================================================
# TASK 4 - FILTER FUNCTIONALITY
# ============================================================

elif menu == "Filter Data":

    st.header("Filter Records")

    c1, c2, c3 = st.columns(3)

    with c1:
        status = st.selectbox(
            "Validation Status",
            ["All"] + sorted(df["Validation_Status"].unique().tolist())
        )

    with c2:
        country = st.selectbox(
            "Country",
            ["All"] + sorted(df["Country"].unique().tolist())
        )

    with c3:
        priority = st.selectbox(
            "Priority",
            ["All"] + sorted(df["Priority"].unique().tolist())
        )

    filtered = df.copy()

    if status != "All":
        filtered = filtered[filtered["Validation_Status"] == status]

    if country != "All":
        filtered = filtered[filtered["Country"] == country]

    if priority != "All":
        filtered = filtered[filtered["Priority"] == priority]

    st.write(f"Records Found: {len(filtered)}")
    st.dataframe(filtered, use_container_width=True)

# ============================================================
# TASK 5 - METRICS DASHBOARD
# ============================================================

elif menu == "Metrics Dashboard":

    st.header("Business Metrics")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Total Biomarkers", len(df))
    c2.metric(
        "Validated",
        len(df[df["Validation_Status"] == "Validated"])
    )
    c3.metric(
        "Pending",
        len(df[df["Validation_Status"] == "Pending"])
    )
    c4.metric(
        "High Priority",
        len(df[df["Priority"] == "High"])
    )
    c5.metric(
        "Total Samples",
        int(df["Sample_Count"].sum())
    )

# ============================================================
# TASK 6 - INSIGHTS DASHBOARD
# ============================================================

elif menu == "Insights Dashboard":

    st.header("Research Insights")

    most_disease = df["Disease"].value_counts().idxmax()
    most_researcher = df["Researcher_Name"].value_counts().idxmax()
    top_country = df["Country"].value_counts().idxmax()

    high_expression = df.loc[
        df["Expression_Level"].idxmax(),
        "Biomarker_Name"
    ]

    high_samples = df.loc[
        df["Sample_Count"].idxmax(),
        "Biomarker_Name"
    ]

    st.success(f"Most Studied Disease: {most_disease}")
    st.success(f"Most Active Researcher: {most_researcher}")
    st.success(f"Top Country: {top_country}")
    st.success(f"Highest Expression Biomarker: {high_expression}")
    st.success(f"Highest Sample Count Biomarker: {high_samples}")

# ============================================================
# TASK 7 - BIOMARKER HEALTH SCORE
# ============================================================

elif menu == "Health Score":

    st.header("Biomarker Health Score")

    health_df = df.copy()

    health_df["Health_Score"] = (
        health_df["Expression_Level"] * 0.6 +
        (health_df["Sample_Count"] / 10) * 0.4
    ).round(2)

    def classify(score):
        if score >= 70:
            return "High"
        elif score >= 40:
            return "Medium"
        return "Low"

    health_df["Score_Tier"] = health_df["Health_Score"].apply(classify)

    st.dataframe(
        health_df.sort_values(
            "Health_Score",
            ascending=False
        ),
        use_container_width=True
    )

    best = health_df.loc[health_df["Health_Score"].idxmax()]

    st.metric(
        "Top Biomarker",
        best["Biomarker_Name"]
    )
    st.metric(
        "Health Score",
        best["Health_Score"]
    )
