from xml.etree.ElementTree import Element

import streamlit as st
import pandas as pd
import numpy as np
import time

from huggingface_hub import upload_file

df = pd.DataFrame({'Customers': ['Ted','Dorothy','Vegas', 'Tony']})
df2 = pd.DataFrame({'Customers': [23, 44, 87, 29]})

st.title("Malt Marbles")
st.header("Self-love, No")
st.subheader('*This has been the unofficial piglet*')
st.text('*You do not have to read this if you have read it*')
st.markdown("< h1 style = 'text-align : center;'>Heading Element </h1>")
st.dataframe(df)
# st.table(df)
# st.json(df)
st.button('Analyze')
st.slider('Select how good it feels',1, 10)
st.selectbox('Select a category', ["Chris","Terry","Anna", "Tedd"])
if st.checkbox('Show data'):
    st.write('Selection saved')

option = st.radio("Choose a category", ['A','B','C'])
time = st.time_input("Select a time")

upload_file = st.file_uploader("Choose a file")
if upload_file is None:
    st.write("File uploaded successfully")

user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello {user_input}! You are about to witness pure voodoo!")
st.text_area("Type your message here:")

number = st.number_input("Insert a number", min_value = 0, max_value = 100, step = 1)

multi_select = st.multiselect("Multiple selections required", ['Option A', 'Option B', 'Option C'])

# Image addition
# st.image("")

# st.line_chart(df2)
st.bar_chart(df2)
# st.area_chart(df2)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1,2,3],[10,20,30])
st.pyplot(fig)

st.sidebar.header("Sidebar Section")
st.sidebar.slider("Adjust parameter", 0, 10)

col1, col2 = st.columns(2)

with col1:
    st.write("Column 1 content")
with col2:
    st.write("Column 2 content")

with st.expander('See more details'):
    st.write("Here you can add more problems")

