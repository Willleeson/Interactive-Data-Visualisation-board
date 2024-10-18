import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Interactive Data Visualization Dashboard",
    layout="wide",
)

# Title and description
st.title("📊 Interactive Data Visualization Dashboard")
st.markdown("""
Upload your dataset and explore various interactive visualizations including bar charts, line graphs, scatter plots, and distribution plots.
""")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File successfully uploaded!")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Awaiting for CSV file to be uploaded.")

# Display DataFrame
if uploaded_file is not None:
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Sidebar for plot settings
    st.sidebar.header("Visualization Settings")

    plot_type = st.sidebar.selectbox(
        "Select Plot Type",
        ("Bar Chart", "Line Graph", "Scatter Plot", "Distribution Plot")
    )

    if plot_type == "Bar Chart":
        st.sidebar.subheader("Bar Chart Settings")
        x_axis = st.sidebar.selectbox("X-axis", df.columns)
        y_axis = st.sidebar.selectbox("Y-axis", df.columns)
        color = st.sidebar.selectbox("Color", df.columns, index=df.columns.tolist().index(df.columns[-1]))

    elif plot_type == "Line Graph":
        st.sidebar.subheader("Line Graph Settings")
        x_axis = st.sidebar.selectbox("X-axis", df.columns)
        y_axis = st.sidebar.selectbox("Y-axis", df.columns)
        color = st.sidebar.selectbox("Color", df.columns, index=df.columns.tolist().index(df.columns[-1]))

    elif plot_type == "Scatter Plot":
        st.sidebar.subheader("Scatter Plot Settings")
        x_axis = st.sidebar.selectbox("X-axis", df.columns)
        y_axis = st.sidebar.selectbox("Y-axis", df.columns)
        color = st.sidebar.selectbox("Color", df.columns, index=df.columns.tolist().index(df.columns[-1]))

    elif plot_type == "Distribution Plot":
        st.sidebar.subheader("Distribution Plot Settings")
        column = st.sidebar.selectbox("Select Column", df.select_dtypes(include=['float', 'int']).columns)
        bins = st.sidebar.slider("Number of Bins", min_value=5, max_value=100, value=30)

    # Generate and display plots
    st.subheader(plot_type)

    if plot_type == "Bar Chart":
        fig = px.bar(df, x=x_axis, y=y_axis, color=color, title=f"Bar Chart of {y_axis} by {x_axis}")
        st.plotly_chart(fig, use_container_width=True)

    elif plot_type == "Line Graph":
        fig = px.line(df, x=x_axis, y=y_axis, color=color, title=f"Line Graph of {y_axis} over {x_axis}")
        st.plotly_chart(fig, use_container_width=True)

    elif plot_type == "Scatter Plot":
        fig = px.scatter(df, x=x_axis, y=y_axis, color=color, title=f"Scatter Plot of {y_axis} vs {x_axis}")
        st.plotly_chart(fig, use_container_width=True)

    elif plot_type == "Distribution Plot":
        fig = px.histogram(df, x=column, nbins=bins, title=f"Distribution of {column}")
        st.plotly_chart(fig, use_container_width=True)

    # Download button
    st.markdown("---")
    st.markdown("### 📥 Download Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='data.csv',
        mime='text/csv',
    )