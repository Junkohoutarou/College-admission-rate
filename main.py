import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Gender Prediction Based on Vietnamese full Names ")

#image = Image.open("vinames.png")
#st.image(image)

nput_model = open('lr_admit.pkl', 'rb')
model = pkl.load(input_model)

st.header('Input addmission information')
gre = st.number_input('Insert GRE Score')
toefl = st.number_input('Insert TOEFL Score')
uni_rate = st.number_input('Insert University Rating')
sop = st.number_input('Insert SOP')
lor = st.number_input('Insert LOR')
cgpa = st.number_input('Insert CGPA')
research =st.radio('Choose Research',[0,1], index=None')
