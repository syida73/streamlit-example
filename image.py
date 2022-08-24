%%writefile myfirstapp.py
import streamlit as st
import numpy as np
import pandas as pd

image = Image.open('https://bouqs.com/blog/wp-content/uploads/2021/11/iris-flower-meaning-and-symbolism.jpg')


st.image(image, caption='Sunset view')
