
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Gender,Customer_Age,Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct,Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[Gender,Customer_Age,Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct,Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio]])
    print(prediction)
    return prediction



def main():
    st.title("Bank Customer Churn Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Bank Customer Churn Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Gender=st.text_input("Gender     [Male=0 and Female=1]")
    Customer_Age=st.text_input("Customer_Age")
    Total_Amt_Chng_Q4_Q1 = st.text_input("Total_Amt_Chng_Q4_Q1")
    Total_Trans_Amt = st.text_input("Total_Trans_Amt")
    Total_Trans_Ct = st.text_input("Total_Trans_Ct")
    Total_Ct_Chng_Q4_Q1 = st.text_input("Total_Ct_Chng_Q4_Q1")
    Avg_Utilization_Ratio = st.text_input("Avg_Utilization_Ratio")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Gender,Customer_Age,Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct,Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio)
        if result[0] == 0:
            st.success('This customer is less likely to cancel the subscription !')
        else:
            st.warning('Warning ! This customer is more likely to cancel the subscription !')
    st.success('The output is {}'.format(result))


    if st.button("About"):
        st.text("Project Guide :-   Dr.Ashwini Patil Mam")
        st.text("Project Members -:  1.Vaishnavi Rajput  2.Purva Rane  3.Rajesh Rampure  4.Venktesh Ranvirkar")

if __name__=='__main__':
    main()
    