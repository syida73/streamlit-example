#importing streamlit library

import streamlit as st

from PIL import Image



#opening the image

image = Image.open('https://bouqs.com/blog/wp-content/uploads/2021/11/iris-flower-meaning-and-symbolism.jpg')



#displaying the image on streamlit app

st.image(image, caption='Sunset view')