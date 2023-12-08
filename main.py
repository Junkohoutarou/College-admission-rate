import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Gender Prediction Based on Vietnamese full Names ")

#image = Image.open("vinames.png")
#st.image(image)

nput_model = open('lrc_admit.pkl', 'rb')
model = pkl.load(input_model)

st.header('Input addmit')
