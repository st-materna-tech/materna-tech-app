import streamlit as st
import joblib
from PIL import Image
import pandas as pd
import numpy as np

    
def predict_sentiment(text): #, model_type):

    # Load the trained model from the local file system
    # if model_type == 'Decision Tree':
        # model_file = "./models/DecisionTreeClassifier.joblib"
    # elif model_type == 'Random Forest':
        # model_file = "./models/RandomForestClassifier.joblib"
    # elif model_type == 'Logistic Regression':
        # model_file = "./models/LogisticRegression.joblib"
    # elif model_type == 'Bagging':
        # model_file = "./models/BaggingClassifier.joblib"
    # elif model_type == 'SVM':
        # model_file = "./models/SVC.joblib" 
        
    model_file = "./models/DecisionTreeClassifier.joblib"   
    # load fitted model
    model = joblib.load(model_file)
    # if model_file in ["./models/MultinomialNB.joblib",  "./models/KNeighborsClassifier.joblib"]:
        # vectorizer = joblib.load('./models/vectorizer.joblib')
        # X_test = vectorizer.transform(text.split())
        # proba = model.predict_proba(X_test)[0]
    # else:
    toPredictDF = pd.read_csv('./final3.csv')
    # toPredictDF = data.drop(columns=['BIRTHDATE', 'DEATHDATE', 'HEALTHCARE_EXPENSES'])
    data_to_predict = toPredictDF[toPredictDF['NEW_PATIENT_ID'] == text].drop(['PATIENT_ID', 'NEW_PATIENT_ID', 'DESCRIPTION'], 1)
    
    proba = model.predict_proba([data_to_predict.iloc[0]]) #data_to_predict .sample(1))[0]
    cats = ['Fetus with unknown complication',
            'Miscarriage in first trimester',
            'Normal pregnancy',
            'Preeclampsia',
            'Tubal pregnancy']

    pred_df = pd.DataFrame({'Categories': cats, 'Probability': proba[0]})
    
    prediction = cats[np.argmax(proba)]
    print(prediction, np.argmax(proba))
    sentiment = "Positive" if prediction == 'Normal pregnancy' else 'Negative' if prediction == 'Miscarriage in first trimester' else "Neutral" 
    return pred_df, sentiment, prediction

def render_page():
    st.title("MATERNATECH")
    st.markdown("---")
    
    st.subheader("Pregnancy Complications Prediction")
    st.text("Your trusted companion for a healthy pregnancy journey")
    st.text("")
    
    # Add sample ids
    # sample_ids = ['b58731cc-2d8b-4c2d-b327-4cab771af3ef', 
                    # '7e4e6d32-15cd-4d5f-a4cc-e5c95ab35eb0',
                    # 'e974e5c3-9b22-41f2-b3a3-c12848f29a73',
                    # '83719bd7-7a41-4c87-93f9-c5de4db6a14a', 
                    # 'f1678bde-4814-4d71-bca9-18fdf5282232',
                    # 'f9b8f463-595a-49c5-8c5a-18ec493301fb']
                    
    sample_ids = ['MTID 9773', 'MTID 1155', 'MTID 7210', 'MTID 2393', 'MTID 5585', 'MTID 1412']
    user_text = st.selectbox('Select a Patiend ID from the list or enter any known Patient IDs', ['Enter Patient ID'] + sample_ids)
    
    # Add text input
    if user_text == 'Enter Patient ID':
        user_text = st.text_input('',placeholder='Enter Patient ID')
        
    st.text("")
    #model_type = st.selectbox('Select a Model', ['Random Forest', 'Decision Tree', 'Logistic Regression', 'Bagging', 'SVM'])
    if st.button('Predict'):
        if user_text:
            pred_df, sentiment, prediction = predict_sentiment(user_text) #, model_type)
            
            st.write('## Result')
            #st.write('---')               
            col1, col2  = st.columns([1, 1]) #, 1])
            with col1:
                print(pred_df)
                st.dataframe(pred_df)
            with col2:
                st.write('Model Prediction:')
                if prediction == 'Normal pregnancy':
                    st.success(prediction)
                elif prediction == 'Miscarriage in first trimester':
                    st.error(prediction)
                else:
                    st.warning(prediction)
