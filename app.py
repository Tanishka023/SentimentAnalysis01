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

# Explicitly set the matplotlib backend for Streamlit
import matplotlib
matplotlib.use('Agg')

# Custom NLTK data directory for compatibility with Streamlit Cloud or other environments
nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")

# Create the directory if it doesn't exist
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

# Set NLTK data path
nltk.data.path.append(nltk_data_dir)

# Ensure the necessary NLTK resources are downloaded
def download_nltk_resources():
    try:
        # Check if punkt tokenizer is downloaded
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', download_dir=nltk_data_dir)

    try:
        # Check if stopwords are downloaded
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', download_dir=nltk_data_dir)

    try:
        # Check if vader lexicon is downloaded
        nltk.data.find('vader_lexicon')
    except LookupError:
        nltk.download('vader_lexicon', download_dir=nltk_data_dir)

    try:
        # Check if wordnet is downloaded
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet', download_dir=nltk_data_dir)

# Call the function to ensure resources are available
download_nltk_resources()

# Load stopwords once
stop_words = set(stopwords.words('english'))

# Function to process text
def process_text(text):
    try:
        # Convert text to lowercase and remove punctuation
        lower_case = text.lower()
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

        # Tokenize words
        tokenized_words = word_tokenize(cleaned_text)

        # Remove stopwords and lemmatize words
        lemmatizer = WordNetLemmatizer()
        final_words = [word for word in tokenized_words if word not in stop_words]
        lemma_words = [lemmatizer.lemmatize(word) for word in final_words]

        # Extract emotions from emotions.txt file
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

        # Count emotion occurrences
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
        st.error(f"An error occurred while processing the text: {e}")
        return None, None


# Streamlit UI
st.title("Text Emotion & Sentiment Analyzer")

# File uploader for text file
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

# If a file is uploaded, process it
if uploaded_file is not None:
    try:
        # Read and decode the uploaded file
        text = uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        st.error("Please upload a UTF-8 encoded text file.")
        text = ""

    if text:
        # Process the uploaded text
        emotions, sentiment = process_text(text)

        # If the emotions and sentiment are successfully processed
        if emotions and sentiment:
            st.subheader("Sentiment:")
            st.write(sentiment)

            st.subheader("Emotions Detected:")
            st.write(dict(emotions))

            # Plotting the emotions
            if emotions:
                fig, ax = plt.subplots()
                ax.bar(emotions.keys(), emotions.values())
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig)
