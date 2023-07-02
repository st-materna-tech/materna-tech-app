import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

def show():
    with st.sidebar:
        image = Image.open('maternatech-high-resolution-logo-black-on-white-background.png')
        #image = image.resize((300, 200))
        st.sidebar.image(image, use_column_width =True)
        st.markdown("""
                    # Applications
                    """, unsafe_allow_html = False)
        selected = option_menu(
            menu_title = None, #required
            # options = ["Text", "IMDb movie reviews", "Image", "Audio", "Video", "Twitter Data", "Web Scraping"], #required
            # icons = ["card-text", "film", "image", "mic", "camera-video", "twitter", "globe"], #optional
            
            options = ["Data Analysis", "Pregnancy Complications Prediction"], #required
            icons = ["image", "card-text"], #optional
            
            # menu_icon="cast", #optional
            default_index = 0, #optional
        )
        return selected