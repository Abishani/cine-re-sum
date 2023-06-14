import streamlit as st
import imdb_api_call as imdb_api_call
import base64

# =============================== Display UI ============================
# =============================== Display Home page ============================

st.set_page_config(
    page_title="cineresum",
    page_icon="📽️",
)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('background_image.png')


st.markdown("<h1 style=' font-family: Comic Sans MS; font-size: 60px; color: #FFFFFF;'>Welcome to CineReSum</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: left; font-family: Comic Sans MS; font-size: 25px;color: #FFFFFF;'>Tired of lengthy movie reviews?\nDiscover the magic of instant movie review summaries in seconds.</p>", unsafe_allow_html=True)


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


st.divider()

# adding attribution
url = 'https://www.imdb.com/'
st.markdown(
    f'''<p style='text-align: center;font-size: 15px;color: #FFFFFF;'>This product uses the IMDb API but is not endorsed or certified by<a href={url}> IMDb</a>.</p>''', unsafe_allow_html=True)
