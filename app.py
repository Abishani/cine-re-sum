import streamlit as st
import imdb_api_call as imdb_api_call


# =============================== Display UI ============================
# =============================== Display Home page ============================
# def home():

st.title("CineReSum 📽️")
st.markdown(
    "Tired of lengthy movie reviews? Discover the magic of instant movie review summaries in seconds.")
# st.sidebar.success("Select here")

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
    f'''This product uses the IMDb API but is not endorsed or certified by<a href={url}> IMDb</a>.''', unsafe_allow_html=True)

st.image("imdb.png", width=100)
