import streamlit as st
from PIL import Image

# 사이드바 화면
st.sidebar.title("sidebar")
st.sidebar.header("type something")
user_id = st.sidebar.text_input("ID: ", 
                                placeholder="streamlit", 
                                max_chars=16, )
user_pw = st.sidebar.text_input("PW: ", 
                                placeholder="1234", 
                                type="password")

st.title("Welcome to Streamlit Sidebar!")

if (user_id == "streamlit") & (user_pw == "1234"):
    st.sidebar.header("Select Box")
    sel_opt = ["Girl with A Pearl Earring", 
            "The Starry Night", 
            "The Scream", 
            "월하정인"]
    user_opt = st.sidebar.selectbox("Which picture do you like the most?", 
                                    sel_opt)
    st.sidebar.write("You selected: ", user_opt)
        
    # 메인 화면
    st.header("Cool Paintings :sunglasses:")
    folder = "data/"
    image_files = ["Vermeer.png", "Gogh.png", "Munch.png", "ShinYoonbok.png"]


    i = sel_opt.index(user_opt)
    img_path = folder + image_files[i]
    img = Image.open(img_path)
    st.image(img, caption=user_opt)
