import streamlit as st
from PIL import Image


logo=Image.open("logo.png")

st.set_page_config(page_title="Coursify · AmazingSells", page_icon=logo, layout='wide')

st.title("Projects")
