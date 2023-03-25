# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 00:16:48 2023

@author: rupes
"""

import numpy as np
import pickle
import streamlit as st

load_model=pickle.load(open('C:/Users/rupes/OneDrive/Desktop/diebetes/trained_diabetes.sav','rb'))

def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the input data
    #std_data = scaler.transform(input_data_reshaped)
    #print(std_data)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return ('The person is not diabetic')
    else:
      return ('The person is diabetic')
  
def main():
    st.title('diebetes prediction web app')

    
    Pregnancies=st.text_input('number of pregancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('BloodPressure level')
    SkinThickness=st.text_input('SkinThickness value')
    Insulin=st.text_input('Insulin value')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
    Age=st.text_input('Age')
    
    #code for prediction
    r=''
    
    #creating button for prediction
    if st.button("test diabetes"):
        r=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(r)
    
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    