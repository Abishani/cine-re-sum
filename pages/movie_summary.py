import streamlit as st
import imdb_api_call as imdb_api_call
import base64

# =============================== Display UI ============================
# =============================== Display Home page ============================

st.markdown("<h1 style='text-align: center;font-family: Comic Sans MS; font-size: 50px; color: #7395a3;'>CineReSum📽️</h1>", unsafe_allow_html=True)


movie_name = st.text_input("Enter the movie name 👇")

# ========================== summarize button ==========================
if st.button("Summarize"):
    imdb_api_call.API_call(movie_name)


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
    f'''<p style='text-align: center;font-size: 15px;'>This product uses the IMDb API but is not endorsed or certified by<a href={url}> IMDb</a>.</p>''', unsafe_allow_html=True)
