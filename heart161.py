# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:54:30 2021

@author: VIDYA
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()


from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("logheart.pkl","rb")
log1=pickle.load(pickle_in)


#@app.route('/')
def welcome():
    return "Welcome All"



#@app.route('/predict',methods=["Get"])
def predict_note_authentication(age,sex,cp,trestbps,chol,thalach,exang,oldpeak,ca):
    
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
        type: numberS
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
    input=np.array([[age,sex,cp,trestbps,chol,thalach,exang,oldpeak,ca]]).astype(np.float64)
    prediction=log1.predict(input)
    print(prediction)
    return prediction
    def test():
        st.info("The person has high risk of having heart disease")
        
    def test2():
        st.info("The person has low risk of having heart disease")


       



def main():
    st.title("Heart failure prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart failure prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age"," ")
    sex = st.text_input("sex(0/1)"," ")
    cp = st.text_input("cp(0/1/2/3)"," ")
    trestbps = st.text_input("testbps(94-200)"," ")
    chol = st.text_input("chol(126-564)"," ")
    thalach = st.text_input("thalach(71-202)"," ")
    exang = st.text_input("exang(0/1)"," ")
    oldpeak= st.text_input("oldpeak(0-6.2)"," ")
    ca = st.text_input("ca(0-3)"," ")
    result=""
    if st.button("Predict"):
        result= predict_note_authentication(age,sex,cp,trestbps,chol,thalach,exang,oldpeak,ca)
        
    st.success('The output is {}'.format(result))
    
    if result == 0:
        st.text('The person has low of heart disease')
    if result ==1:
        st.text('The person has high of heart disease')
    
    
    

    
    
        
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    