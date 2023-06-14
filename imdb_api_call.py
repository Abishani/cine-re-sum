import streamlit as st
import requests
import secrets_1 as py_secrets
import summarize as summarization_model

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

                col1, col2 = st.columns(2, gap="large")
                # Display the movie image if available, else display "Image not found"

                with col1:
                    if search_results[0]['image']:
                        st.image(search_results[0]['image'], width=300)
                    else:
                        st.write("Image not found")

                # Retreive the movie ratings using the ratings endpoint

                with col2:
                    st.markdown("""
                    <style>
                    .big-font {
                        font-size:20px !important;
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    ratings_url = f'https://imdb-api.com/en/API/Ratings/{API_KEY}/{movie_id}'
                    ratings_response = requests.get(ratings_url).json()

                    if ratings_response['errorMessage']:
                        print(ratings_response['errorMessage'])
                        st.write('No ratings found for this movie')
                    else:

                        imdb_rating = ratings_response['imDb']
                        rotten_tomatoes_rating = ratings_response['rottenTomatoes']
                        metacritic_rating = ratings_response['metacritic']

                    # redirecting to websites
                    external_link = f'https://imdb-api.com/en/API/ExternalSites/{API_KEY}/{movie_id}'
                    link_response = requests.get(external_link).json()

                    if link_response['errorMessage']:
                        print(link_response['errorMessage'])
                        st.write('No any ratings are available for this movie')

                    elif link_response:
                        imdb = link_response['imDb']['url']
                        rotten_tomatoes = link_response['rottenTomatoes']['url']
                        metacritic = link_response['metacritic']['url']

                        st.markdown(
                            f'<p class="big-font">IMDb Rating: <a href={imdb}><b>⭐{imdb_rating}</b> /10</a></p>', unsafe_allow_html=True)
                        st.markdown(
                            f'<p class="big-font">Rotten Tomatoes Rating:<a href={rotten_tomatoes}> <b>🍅{rotten_tomatoes_rating}</b>% </a></p>', unsafe_allow_html=True)
                        st.markdown(
                            f'<p class="big-font">Metacritics Rating:<a href={metacritic}><b>🟩{metacritic_rating}</b>% </a></p>', unsafe_allow_html=True)
                    else:
                        st.markdown(
                            f'<p class="big-font">IMDb Rating: <b>⭐{imdb_rating}</b> /10</p>', unsafe_allow_html=True)
                        st.markdown(
                            f'<p class="big-font">Rotten Tomatoes Rating: <b>🍅{rotten_tomatoes_rating}</b>% </p>', unsafe_allow_html=True)
                        st.markdown(
                            f'<p class="big-font">Metacritics Rating:<b>🟩{metacritic_rating}</b>% </p>', unsafe_allow_html=True)

                summary = summarization_model.pegasus_summarize(
                    "\n".join(reviews))
                st.write("Summary: ")
                st.write(summary)

        else:
            print('No search results found.')
            st.write("Movie is not found. Please enter a different movie.")
