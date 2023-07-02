import streamlit as st
from PIL import Image
import pandas as pd


def render_page():
    st.title("Data Analysis")
    
    st.header('Sample Dataset')
    col1 = st.columns(1)
    final_df = pd.read_csv("final2.csv")
    st.dataframe(final_df.sample(5))
    
    st.header("Class Distribution Charts")
    
    # Load the saved plots as PIL images
    dist_plot1 = Image.open("./images/class distribution.png")
    dist_plot2 = Image.open("./images/category_dist.png")

    # Display the images using st.image
    
    col1, col2 = st.columns([2,3])
    col1.image(dist_plot1, caption="Class distribution", use_column_width=True)
    col2.image(dist_plot2, caption="Character distribution")
    
    
    
    # Load the saved plots as PIL images
    text_plot1 = Image.open("./images/by_age.png")
    text_plot2 = Image.open("./images/by_body_weight.png")
    text_plot3 = Image.open("./images/by_marital_status.png")
    text_plot4 = Image.open("./images/by_race.png")
    text_plot5 = Image.open("./images/by_smoke_status.png")
    text_plot6 = Image.open("./images/health_exp.png")
    

    st.header("Bi-Variate Charts")
    
    # Define the plots
    plots = [text_plot1, text_plot2, text_plot3, text_plot4, text_plot5, text_plot6]

    # Create a grid of columns with 2 columns in each row
    num_plots = len(plots)
    num_columns = 2
    num_rows = (num_plots + 1) // 2  # Round up to the nearest integer

    for row in range(num_rows):
        cols = st.columns(num_columns)
        for col, plot_index in zip(cols, range(row * num_columns, min((row + 1) * num_columns, num_plots))):
            col.image(plots[plot_index], use_column_width=True)
            
            
    st.header("Model Evaluation")
    
    # Load the saved plots as PIL images
    dist_plot1 = Image.open("./images/models_acc_comp.png")
    dist_plot2 = Image.open("./images/conf_matrix.png")

    # Display the images using st.image
    col1, col2 = st.columns([2,3])
    col1.image(dist_plot1, caption="Accuracy Evluation", use_column_width=True)
    col2.image(dist_plot2, caption="Confusion Matrif of the best model")