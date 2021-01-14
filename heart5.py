# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:58:22 2021

@author: VIDYA
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("log1.pkl","rb")
log2=pickle.load(pickle_in)

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
   
    input=np.array([[age,sex,cp,trestbps,chol,thalach,exang,oldpeak,ca]]).astype(np.float64)
    prediction=log2.predict(input)
    print(prediction)
    return prediction


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","Type Here")
    sex = st.text_input("sex(0/1)","Type Here")
    cp = st.text_input("cp(0/1/2/3)","Type Here")
    trestbps = st.text_input("testbps(94-200)","Type Here")
    chol = st.text_input("chol(126-564)","Type Here")
    thalach = st.text_input("thalach(71-202)","Type Here")
    exang = st.text_input("exang(0/1)","Type Here")
    oldpeak= st.text_input("oldpeak(0-6.2)","Type Here")
    ca = st.text_input("ca(0-3)","Type Here")
    result=""
    if st.button("Predict"):
        
        result = predict_note_authentication(age, sex, cp, trestbps, chol, thalach, exang, oldpeak, ca)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()