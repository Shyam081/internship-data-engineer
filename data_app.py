import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("📊 Mini Data Analyzer App")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read data
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    st.subheader("Basic Information")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Column selection for visualization
    st.subheader("📈 Create a Visualization")
    x_col = st.selectbox("Choose X-axis column:", df.columns)
    y_col = st.selectbox("Choose Y-axis column:", df.columns)

    if st.button("Show Chart"):
        fig = px.bar(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
        st.plotly_chart(fig)
else:
    st.info("👆 Upload a CSV file to get started.")
