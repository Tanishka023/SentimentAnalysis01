import streamlit as st
import string
from collections import Counter
import matplotlib.pyplot as plt
import nltk
import os

from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, wordpunct_tokenize

# Explicitly set matplotlib backend
import matplotlib
matplotlib.use('Agg')

# Custom NLTK data directory
nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

nltk.data.path.append(nltk_data_dir)

# Force download necessary resources
def download_nltk_resources():
    resources = {
        'punkt': 'tokenizers/punkt',
        'stopwords': 'corpora/stopwords',
        'vader_lexicon': 'sentiment/vader_lexicon',
        'wordnet': 'corpora/wordnet'
    }
    for resource, path in resources.items():
        try:
            nltk.data.find(path)
        except LookupError:
            nltk.download(resource, download_dir=nltk_data_dir, force=True)

# Call to ensure resources
download_nltk_resources()

# Load stopwords
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    st.error("Failed to load NLTK stopwords.")

# Text processing function
def process_text(text):
    try:
        # Lowercase & remove punctuation
        lower_case = text.lower()
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

        # Tokenize words using safer tokenizer
        tokenized_words = wordpunct_tokenize(cleaned_text)

        # Remove stopwords & lemmatize
        lemmatizer = WordNetLemmatizer()
        final_words = [word for word in tokenized_words if word not in stop_words]
        lemma_words = [lemmatizer.lemmatize(word) for word in final_words]

        # Emotion detection
        file_path = os.path.join(os.path.dirname(__file__), 'emotions.txt')
        emotion_list = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    clean_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                    word, emotion = clean_line.split(':')
                    if word in lemma_words:
                        emotion_list.append(emotion)
        else:
            st.error("emotions.txt file not found!")
            return None, None

        # Count emotions
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

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

# Streamlit UI
st.title("Text Emotion & Sentiment Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

# Manual re-download button for debugging
if st.button("Force Redownload NLTK Resources"):
    download_nltk_resources()
    st.success("Redownloaded NLTK resources.")

# Process uploaded text
if uploaded_file is not None:
    try:
        text = uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        st.error("Please upload a UTF-8 encoded text file.")
        text = ""

    if text:
        emotions, sentiment = process_text(text)

        if emotions and sentiment:
            st.subheader("Sentiment:")
            st.write(sentiment)

            st.subheader("Emotions Detected:")
            st.write(dict(emotions))

            # Plot
            if emotions:
                fig, ax = plt.subplots()
                ax.bar(emotions.keys(), emotions.values(), color='skyblue')
                plt.xticks(rotation=45, ha='right')
                plt.title("Emotion Distribution")
                plt.xlabel("Emotions")
                plt.ylabel("Count")
                st.pyplot(fig)
