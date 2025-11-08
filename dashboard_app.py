import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# PAGE CONFIGURATION
# -------------------------
st.set_page_config(
    page_title="📊 Data Dashboard App",
    layout="wide",
)

st.title("📈 Interactive Data Dashboard")

# -------------------------
# SIDEBAR SECTION
# -------------------------
st.sidebar.header("Upload & Filter Options")

uploaded_file = st.sidebar.file_uploader("📁 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show basic info
    st.sidebar.subheader("Data Filters")
    all_columns = df.columns.tolist()

    # Optional filters
    selected_columns = st.sidebar.multiselect("Select columns to display", all_columns, default=all_columns)
    df = df[selected_columns]

    # Numeric filter example
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    if numeric_cols:
        num_col = st.sidebar.selectbox("Filter by numeric column", numeric_cols)
        min_val, max_val = float(df[num_col].min()), float(df[num_col].max())
        filter_range = st.sidebar.slider("Select range", min_val, max_val, (min_val, max_val))
        df = df[(df[num_col] >= filter_range[0]) & (df[num_col] <= filter_range[1])]

    # -------------------------
    # MAIN CONTENT
    # -------------------------
    st.subheader("📋 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    # -------------------------
    # VISUALIZATION
    # -------------------------
    st.subheader("📉 Create a Visualization")

    chart_type = st.selectbox(
        "Select chart type",
        ["Bar", "Line", "Scatter", "Pie"]
    )

    x_col = st.selectbox("Select X-axis", df.columns)
    y_col = st.selectbox("Select Y-axis", df.columns)

    if st.button("Generate Chart"):
        if chart_type == "Bar":
            fig = px.bar(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
        elif chart_type == "Line":
            fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
        elif chart_type == "Pie":
            fig = px.pie(df, names=x_col, values=y_col, title=f"{y_col} by {x_col}")
        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("👆 Upload a CSV file from the sidebar to begin your analysis.")
