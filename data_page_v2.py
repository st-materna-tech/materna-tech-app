import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

def render_page():
    st.title("Data Analysis")
    
    st.header('Sample Dataset')
    col1 = st.columns(1)
    final_df = pd.read_csv("final2.csv")
    bi_df = pd.read_csv("bi-classification2.csv")
    # Read from the conditions.csv file
    df = pd.read_csv("conditions.csv")
    new_df = df[['PATIENT', 'DESCRIPTION']]
    pa_des = new_df[new_df['DESCRIPTION'].isin(["Fetus with unknown complication", "Tubal pregnancy", "Miscarriage in first trimester", "Preeclampsia", "Normal pregnancy"])]
    des_count = pa_des.groupby('DESCRIPTION').size().reset_index(name='count')
    
    
    # Specify the desired column order
    desired_columns = ['PATIENT_ID', 'HEALTHCARE_EXPENSES', 'AGE', 'BIRTHDATE', 'Urea Nitrogen', 'Heart rate', 'Body Weight',
                       'Body Height', 'Calcium', 'Creatinine', 'DALY']

    # Create a new DataFrame with the desired column order
    reordered_df = final_df[desired_columns + [col for col in final_df.columns if col not in desired_columns]]

    # Display the DataFrame
    st.dataframe(reordered_df.sample(5))
    
    st.header("Class Distribution Charts")
    
    dist_plot1 = px.bar(des_count, x="DESCRIPTION", y="count", title="Patients distribution for different complications")
    dist_plot1.update_layout(xaxis_tickangle=-45)
        
     
    # Compute the distribution of Description categories
    description_counts = bi_df['DESCRIPTION'].value_counts()

    # Create the pie chart using Plotly Express
    dist_plot2 = px.pie(values=description_counts.values, names=description_counts.index, title='Distribution of Description Categories',
                 color_discrete_sequence=px.colors.qualitative.Dark2,
                 hole=0.3, labels={'label': 'Category', 'value': 'Count'})

    # Customize the layout
    dist_plot2.update_traces(textposition='inside', textinfo='percent+label',
                      marker=dict(line=dict(color='white', width=2)))
                  
                  
    # st.plotly_chart(fig)
    
    # Load the saved plots as PIL images
    # dist_plot1 = Image.open("./images/class distribution.png")
    # dist_plot2 = Image.open("./images/category_dist.png")

    # Display the images using st.image
    
    col1, col2 = st.columns([1,1])
    col1.plotly_chart(dist_plot1, caption="Class distribution")
    col2.plotly_chart(dist_plot2, caption="Character distribution")
    
    
    
    
    
    text_plot1 = px.histogram(bi_df, x="MARITAL", color="DESCRIPTION", barmode="group",) # color_discrete_sequence=['#FFA500', '#FF8C00'])
    text_plot1.update_layout(title="Pregnency Category by Marital status",
                      xaxis_title="Marital status",
                      yaxis_title="Count")
    
    text_plot2 = px.histogram(bi_df, x="RACE", color="DESCRIPTION", barmode="group", color_discrete_sequence=px.colors.qualitative.Dark2)
    text_plot2.update_layout(title="Pregnency Category in Different Races",
                      xaxis_title="Race",
                      yaxis_title="Count")
     
    text_plot3 = px.histogram(bi_df, x="Tobacco smoking status NHIS", color="DESCRIPTION", barmode="group", color_discrete_sequence=px.colors.sequential.Turbo)
    text_plot3.update_layout(title="Pregnancy Category in Different Smoking Status",
                      xaxis_title="Smoking Status",
                      yaxis_title="Count")
    

    text_plot4 = px.box(bi_df, x="DESCRIPTION", y="HEALTHCARE_EXPENSES", color="DESCRIPTION", color_discrete_sequence=px.colors.sequential.Turbo)
    text_plot4.update_layout(title="Healthcare Expenses on Different Categories",
                      xaxis_title="Categories",
                      yaxis_title="Healthcare Expenses")
    

    text_plot5 = px.violin(bi_df, x="DESCRIPTION", y="Body Weight", color="DESCRIPTION", box=True, points="outliers", color_discrete_sequence=px.colors.sequential.Electric)
    text_plot5.update_layout(title="Body Weight in Different Description Categories",
                      xaxis_title="Description",
                      yaxis_title="Body Weight")
    

    text_plot6 = px.box(final_df, x="DESCRIPTION", y="AGE", color="DESCRIPTION", color_discrete_sequence=px.colors.sequential.Jet)
    text_plot6.update_layout(title="Age in Different Description Categories",
                      xaxis_title="Description",
                      yaxis_title="Age")
                  
    # # Load the saved plots as PIL images
    # text_plot1 = Image.open("./images/by_age.png")
    # text_plot2 = Image.open("./images/by_body_weight.png")
    # text_plot3 = Image.open("./images/by_marital_status.png")
    # text_plot4 = Image.open("./images/by_race.png")
    # text_plot5 = Image.open("./images/by_smoke_status.png")
    # text_plot6 = Image.open("./images/health_exp.png")
    

    st.header("Bi-Variate Charts")
    
    # Define the plots
    plots = [text_plot1, text_plot3, text_plot5, text_plot6]

    # Create a grid of columns with 2 columns in each row
    num_plots = len(plots)
    num_columns = 2
    num_rows = (num_plots + 1) // 2  # Round up to the nearest integer

    for row in range(num_rows):
        cols = st.columns(num_columns)
        for col, plot_index in zip(cols, range(row * num_columns, min((row + 1) * num_columns, num_plots))):
            col.plotly_chart(plots[plot_index], use_column_width=True)
            
            
    st.header("Model Evaluation")
   
    results_df = pd.read_csv('results_df.csv')
    model_plot1 = px.bar(results_df, x='model', y=['Train Accuracy', 'Test Accuracy'], barmode='group', color_discrete_sequence=['skyblue', 'salmon'])
    model_plot1.update_layout(title='Model Performance Comparison', xaxis_title='Model', yaxis_title='Accuracy')

    # Load the saved plots as PIL images
    # model_plot1 = Image.open("./images/models_acc_comp.png")
    model_plot2 = Image.open("./images/conf_matrix.png")

    # Display the images using st.image
    col1, col2 = st.columns([3,3])
    col2.plotly_chart(model_plot1, caption="Accuracy Evluation") #, use_column_width=True)
    #col1.image(model_plot2, caption="Confusion Matrif of the DT Model")
