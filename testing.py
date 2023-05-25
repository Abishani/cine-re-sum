import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import secrets_1 as py_secrets

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



# =============================== Display UI ============================
st.title("CineReSum 📽️")
movie_reviews = st.text_area("Enter the movie reviews 👇")


# ========================== summarize button ==========================
if st.button("Summarize"):
    summary = pegasus_summarize(movie_reviews)
    st.write("Summary:")
    st.write(summary)


# Hide hamburger menu
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
