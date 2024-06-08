import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie


logo = Image.open('C://Users//hp//OneDrive//My files//Python Web//AmazingSells//logo.png')
hm_logo=Image.open('C://Users//hp//OneDrive//My files//Python Web//AmazingSells//Untitled.png')

st.set_page_config(
    page_title="AmazingSells",
    page_icon=logo,
    layout='wide'
)


st.sidebar.success("Select a page above.")


st.markdown("""
  <style>

    /*the main div*/
    .st-emotion-cache-1v0mbdj {
        width: 300px; /*max value according to image width, can be smaller but not larger*/
        height: 300px;
        overflow: hidden;
        border-radius: 50%;
        text-align: center;
    }
    
    /*the img elements in the main div class*/
    .st-emotion-cache-1v0mbdj > img{
        text-align: center;
    }
  
  </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stHeadingContainer {
        text-align: center
    }

    h3 {
        text-align: center;
    }

    .st-emotion-cache-99ud0u {
        text-align: center
    }
    </style>
""", unsafe_allow_html=True)

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

#--Assets---
lottie_coding=load_lottie_url("https://lottie.host/1d017360-8bce-443a-85a0-1eae7564f046/81d5E1RKS7.json")
lottie_pro=load_lottie_url("https://lottie.host/519cfa1c-612f-46f6-8470-8a276b352588/qLz9psrzEa.json")
lottie_email = load_lottie_url("https://lottie.host/df6a2651-b697-40e7-9ee4-301c4977e341/0cYxYFCvsU.json")
lottie_insta=load_lottie_url("https://lottie.host/980c00fa-3458-4ba0-ba1a-5481b50223fc/SBnHYbqbgd.json")

#---Header Section----
with st.container():
    one,two,three = st.columns(3)
    with one:
        st.write('##')
    with two:      
        st.image(hm_logo)
    with three:
        st.write('##')
with st.container():   
    st.subheader("Hi, welcome to AmazingSells official website :wave:")  
    st.title("AmazingSells provide you the best products to buy on the market!")
    st.write("A perfect side hustle to earn money, or a product you are willing to buy at low cost, AmzingSells has got your back. Providing you with exclusive offers and discounts of products to buy online.")
    
#----What I do-----
with st.container():
    st.write("---")
    st.header("What I Do")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            I make websites for business using Python Frameworks or HTML Frameworks. I also make databases for analytic companies using Python and an amazing feature for it - Machine Learning or AI. These features can boost your data analytics and accuracy of them.  

            I also make apps that can shape and help the life of human beings and even animals. I have experience in robotic engineering - Arduino, Raspberry.pi.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=250, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With AmazingSells!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/amazingsells2@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_email, height=300, key="email")
    with right_column:
        st.markdown(contact_form, unsafe_allow_html=True)

st.balloons()

