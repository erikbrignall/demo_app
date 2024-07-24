import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#print('hellow world')
with st.sidebar:
    st.image('TR-logo.png')
    st.subheader('another subheader')



st.header('header 1')
st.divider()

################
st.header('Now this get mores complicated')

with st.form(key='my_form_to_submit'):
    st.write('lets add up pieces of fruit')
    col1, col2, col3 = st.columns(3)
    a = col1.slider('How many organse do we have', min_value = 0, max_value = 50)
    b = col2.slider('How many bananas do we have', min_value = 0, max_value = 50)
    c = col3.slider('How many apples do we have', min_value = 0, max_value = 50)
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    d = a + b + c
    st.subheader(d)

# load a csv
filename = 'benchmarks.csv'
dfB = pd.read_csv(filename)

st.dataframe(dfB)
changevar = '12%'
mean_value1 = dfB['Acceleration'].mean().round(1)
st.metric('av. Acceleration', mean_value1, changevar)


with st.form(key="another_form"):
    st.header('making a graph - brain cells')
    g1, g2, g3, g4 = st.columns(4)
    val1 = g1.number_input('Joe', value=4)
    val2 = g1.number_input('Donald', value=4)
    submit_button2 = st.form_submit_button(label='submit')

if submit_button2:
    braincell_counts = {'joe': val1, 'donald': val2}
    labels = list(braincell_counts.keys())
    values = list(braincell_counts.values()) 
    fig, ax = plt.subplots()
    color = ['blue','red']
    ax.bar(labels, values, color = color)
    st.pyplot(fig)

    #st.bar_chart(braincell_counts)

from PIL import Image

def load_image(image_file):
    img = Image.open(image_file)
    return img

image_file = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'])

if image_file is not None:
    st.image(load_image(image_file),width=250)


st.components.v1.iframe("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2478.074522868566!2d-2.6231365242397446!3d51.60352310367774!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4871952a150f985d%3A0x74252ed449d40a30!2sSevern%20View%20Services!5e0!3m2!1sen!2suk!4v1721815586590!5m2!1sen!2suk", height=400, scrolling=True)

