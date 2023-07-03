import streamlit as st
import sidebar
import predictions_page
import data_page_v2

# Set page configuration
st.set_page_config(layout="wide", page_title="MATERNATECH", page_icon=":baby:")
st.markdown(
"""
<style>
.sidebar .sidebar-content {
background-color: #f8f9fa;
padding: 1rem;
}
.logo {
text-align: center;
margin-bottom: 2rem;
}
.page-title {
text-align: center;
font-size: 32px;
margin-bottom: 2rem;
}
</style>
""",
unsafe_allow_html=True,
)

# Logo and page title
st.markdown('<div class="logo"><h1>MATERNATECH</h1></div>', unsafe_allow_html=True)
st.markdown('<h2 class="page-title">Pregnancy Journey Companion</h2>', unsafe_allow_html=True)

# Render sidebar and corresponding page
page = sidebar.show()

if page == "Pregnancy Complications Prediction":
predictions_page.render_page()
elif page == "Data Analysis":
data_page_v2.render_page()
