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


# Load pre-downloaded NLTK resources
nltk.data.path.append(os.path.join(os.path.dirname(__file__), 'nltk_data'))

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
        final_words = [word for word in tokenized_words if word not in stop_words]
        lemma_words = [WordNetLemmatizer().lemmatize(word) for word in final_words]

        # Extract emotions
        file_path = os.path.join(os.path.dirname(__file__), 'emotions.txt')
        emotion_list = []
        if os.path.exists(file_path):  # Ensure the file exists before opening it
            with open(file_path, 'r') as file:
                for line in file:
                    clean_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                    word, emotion = clean_line.split(':')
                    if word in lemma_words:
                        emotion_list.append(emotion)
        else:
            st.error("Emotions file not found!")
            return None, None

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
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file is not None:
    try:
        # Handle file encoding issues
        text = uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        st.error("Unable to decode the uploaded file. Please ensure it is a valid UTF-8 encoded text file.")
        text = ""

    if text:
        emotions, sentiment = process_text(text)

        if emotions and sentiment:
            st.subheader("Sentiment:")
            st.write(sentiment)

            st.subheader("Emotions Detected:")
            st.write(dict(emotions))

            # Plotting the emotions
            if emotions:
                fig, ax = plt.subplots()
                ax.bar(emotions.keys(), emotions.values())
                plt.xticks(rotation=45)
                st.pyplot(fig)
