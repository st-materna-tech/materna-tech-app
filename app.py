import streamlit as st
import sidebar
import predictions_page
import data_page_v2

st.set_page_config(layout="wide", page_title="MATERNATECH", page_icon=":baby:")

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0.5rem;
                }
        </style>
        """, unsafe_allow_html=True)
        

# st.title("Hello")
page = sidebar.show()

if page=="Pregnancy Complications Prediction":
    predictions_page.render_page()
elif page=="Data Analysis":
    data_page_v2.render_page()
