import streamlit as st
from PIL import Image

greeting = st.title("Welcome to Streamlit Sidebar!")

# 사이드바 화면
st.sidebar.title("sidebar")
st.sidebar.header("type something")
username = st.sidebar.text_input("ID: ", 
                                placeholder="streamlit", 
                                max_chars=16, )
password = st.sidebar.text_input("PW: ", 
                                placeholder="1234", 
                                type="password")


def signed_in():
    greeting.empty()
    st.sidebar.empty()
    logout_btn = st.button("logout")
    st.sidebar.header("Select Box")
    sel_opt = ["Girl with A Pearl Earring", 
            "The Starry Night", 
            "The Scream", 
            "월하정인"]
    user_opt = st.sidebar.selectbox("Which picture do you like the most?", 
                                    sel_opt)
    st.sidebar.write("You selected: ", user_opt)
        
    # 메인 화면
    st.title("Streamlit Sidebar")
    st.subheader("Cool Paintings :sunglasses:")
    folder = "data/"
    image_files = ["Vermeer.png", "Gogh.png", "Munch.png", "ShinYoonbok.png"]

    i = sel_opt.index(user_opt)
    img_path = folder + image_files[i]
    img = Image.open(img_path)
    st.image(img, caption=user_opt)
    
    
    if logout_btn:
        st.toast("Logged out!")


signin_btn = st.sidebar.button("sign in")

if signin_btn:
        if (username == "streamlit") & (password == "1234"):
            st.toast(f"Hello, {username}")
            signed_in()
        else:
            st.error("Invalid username or password")
