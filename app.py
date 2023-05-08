import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import requests
import secrets_1 as py_secrets

# Load Pegasus tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(
    "Abishani/NLP_summarization_model1", use_auth_token=py_secrets.access_token
    #after making the model public remove the use_auth_token parameter
    

)
model = AutoModelForSeq2SeqLM.from_pretrained(
    "Abishani/NLP_summarization_model1", use_auth_token=py_secrets.access_token
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


# =============== API call =====================#
def API_call(movie_name):
    API_KEY = py_secrets.api_key

    # Search for the movie using the SearchMovie endpoint
    search_url = f'https://imdb-api.com/en/API/SearchMovie/{API_KEY}/{movie_name}'
    search_response = requests.get(search_url).json()

    # Get the ID of the first search result
    if search_response['errorMessage']:
        print(search_response['errorMessage'])
    else:
        search_results = search_response['results']
        if search_results:
            movie_id = search_results[0]['id']

            # Retrieve the movie reviews using the Reviews endpoint
            reviews_url = f'https://imdb-api.com/en/API/Reviews/{API_KEY}/{movie_id}'
            reviews_response = requests.get(reviews_url).json()

            # get all the reviews (['items'][i]['content']) and combine it into one string
            reviews = [item["content"] for item in reviews_response["items"]]
            review_text = "\n".join(reviews)

            # summarize the combine reviews and generate the summary using pegasus.summarize()
            summary = pegasus_summarize(review_text)
            st.write("Summary: ")
            st.write(summary)

             #storing the summary in the streamlit using st.cache
            @st.cache
            def save_summary(summary):
                return summary
            save_summary(summary)



        else:
            print('No search results found.')


# =============== Display UI ==================
st.title("CineReSum 📽️")
movie_name = st.text_area("Enter the movie name 👇", height=100)


# summarize button
if st.button("Summarize"):
    API_call(movie_name)



# Hide hamburger menu
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)