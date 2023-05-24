import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import requests
import secrets_1 as py_secrets
import webbrowser

# =========================== Load Pegasus tokenizer and model =============================
tokenizer = AutoTokenizer.from_pretrained(
    "Abishani/amrs-cineresum-summarizer", use_auth_token=py_secrets.access_token
)
model = AutoModelForSeq2SeqLM.from_pretrained(
    "Abishani/amrs-cineresum-summarizer", use_auth_token=py_secrets.access_token
)
max_length = 100
min_length = 80


# =============== PEGASUS Summarization function ==================#
def pegasus_summarize(text):
    tokens = tokenizer(text, truncation=True,
                       padding="longest", return_tensors="pt")
    gen = model.generate(
        **tokens,
        max_length=max_length,
        min_length=min_length,
        do_sample=True,
        num_return_sequences=1,
    )
    summary = tokenizer.decode(gen[0], skip_special_tokens=True)
    return summary


# ======================================= API call ================================= #
def API_call(movie_name):
    API_KEY = py_secrets.api_key

    # Search for the movie using the SearchMovie endpoint
    search_url = f'https://imdb-api.com/en/API/SearchMovie/{API_KEY}/{movie_name}'
    search_response = requests.get(search_url).json()

    # Check if any search results are found
    if search_response['errorMessage']:
        print(search_response['errorMessage'])
        st.write("Movie is not found. Please enter a different movie.")
    else:
        search_results = search_response['results']
        if search_results:
            movie_id = search_results[0]['id']
         # Check if the exact movie is found in the search results
         # exact_movie_found = False
         # for result in search_results:
         #     if movie_name.lower() in result['title'].lower():
         #         exact_movie_found = True
         #         movie_id = result['id']
         #         break

         # if exact_movie_found:
            # Retrieve the movie reviews using the Reviews endpoint
            reviews_url = f'https://imdb-api.com/en/API/Reviews/{API_KEY}/{movie_id}'
            reviews_response = requests.get(reviews_url).json()

            if reviews_response['errorMessage']:
                print(reviews_response['errorMessage'])
                st.write("No reviews found for this movie.")
            else:
                # Get all the reviews (['items'][i]['content']) and combine them into one string
                reviews = [item["content"]
                           for item in reviews_response["items"]]

                # Print the movie name from the API call
                st.title(search_results[0]['title'])

                # Print the count of total reviews
                st.write("Number of Total Reviews:", len(reviews))

                # If "See All Reviews" button is clicked it will redirect to IMDB website
                def open_imdb_website():
                    imdb_link = "https://www.imdb.com/"
                    webbrowser.open(imdb_link)

                st.button("See All Reviews!", on_click=open_imdb_website)

                summary = pegasus_summarize("\n".join(reviews))
                st.write("Summary:")
                st.write(summary)

                # Display the movie image if available, else display "Image not found"
                if search_results[0]['image']:
                    st.image(search_results[0]['image'])
                else:
                    st.write("Image not found")
         # else:
         #     print('Movie not found in the search results.')
         #     st.write("Movie is not found. Please enter a different movie.")
        else:
            print('No search results found.')
            st.write("Movie is not found. Please enter a different movie.")


# =============================== Display UI ============================
st.title("CineReSum 📽️")
movie_name = st.text_input("Enter the movie name 👇")


# ========================== summarize button ==========================
if st.button("Summarize"):
    API_call(movie_name)


# Hide hamburger menu
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
