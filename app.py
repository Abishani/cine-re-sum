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

# adding attribution
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
url = 'https://www.imdb.com/'
st.markdown(
        f'''This product uses the IMDb API but is not endorsed or certified by<a href={url}> IMDb</a>.''', unsafe_allow_html=True)
# col1, col2 = st.columns(2)
# with col1:
st.image("imdb.png",width=100)

# with col2:
#     url = 'https://www.imdb.com/'
#     st.markdown(
#         f'''This product uses the IMDb API but is not endorsed or certified by<a href={url}> IMDb</a>.''', unsafe_allow_html=True)


# =============================== Display Movie Name Enter page ============================
# def summary_generation_page():
# st.title("CineReSum 📽️")
# st.write("Reviews of the movie will be automatically gathered from IMDb and the summary will be provided")
# movie_name = st.text_input("Enter the movie name 👇")

# # ========================== summarize button ==========================
# if st.button("Summarize"):
#     imdb_api_call.API_call(movie_name)
# page_names_to_funcs = {
#     "Home": home,
#     "Summary Generation": summary_generation_page
# }

# demo_name = st.sidebar.selectbox("CineReSum 📽️", page_names_to_funcs.keys())
# page_names_to_funcs[demo_name]()


# # Hide hamburger menu
# hide_menu_style = """
#     <style>
#     #MainMenu {visibility: hidden;}
#     </style>
#     """
# st.markdown(hide_menu_style, unsafe_allow_html=True)
