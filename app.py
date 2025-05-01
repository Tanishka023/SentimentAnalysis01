import streamlit as st
import string
from collections import Counter
import matplotlib.pyplot as plt
import nltk
import os

from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Check and download NLTK resources if they aren't already downloaded
def download_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet')
    try:
        nltk.data.find('vader_lexicon')
    except LookupError:
        nltk.download('vader_lexicon')

# Call the download function
download_nltk_resources()

# Load stopwords once
stop_words = set(stopwords.words('english'))

def process_text(text):
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    tokenized_words = word_tokenize(cleaned_text)  # No need for "english" parameter
    
    final_words = [word for word in tokenized_words if word not in stop_words]
    lemma_words = [WordNetLemmatizer().lemmatize(word) for word in final_words]

    # Extract emotions
    emotion_list = []
    if os.path.exists('emotions.txt'):  # Ensure the file exists before opening it
        with open('emotions.txt', 'r') as file:
            for line in file:
                clean_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clean_line.split(':')
                if word in lemma_words:
                    emotion_list.append(emotion)
    else:
        st.error("Emotions file not found!")

    emotion_counter = Counter(emotion_list)

    # Sentiment analysis
    score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    if score['neg'] > score['pos']:
        sentiment = "Negative Sentiment"
    elif score['neg'] < score['pos']:
        sentiment = "Positive Sentiment"
    else:
        sentiment = "Neutral Sentiment"

    return emotion_counter, sentiment

# Streamlit UI
st.title("Text Emotion & Sentiment Analyzer")
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    emotions, sentiment = process_text(text)

    st.subheader("Sentiment:")
    st.write(sentiment)

    st.subheader("Emotions Detected:")
    st.write(dict(emotions))

    # Plotting
    if emotions:
        fig, ax = plt.subplots()
        ax.bar(emotions.keys(), emotions.values())
        plt.xticks(rotation=45)
        st.pyplot(fig)
