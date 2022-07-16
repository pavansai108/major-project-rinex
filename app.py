import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('ds_salaries(1)')

#user input 
st.title("Employment experience level SE-Senior,EX-experienced,MI-medium")
ip = st.text_input("Enter your message:") 
op = model_nb.predict([ip])
if st.button('Predict'):
  st.title(op[0])  

      
                                    
  
 
