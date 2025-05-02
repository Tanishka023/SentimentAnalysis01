Text Emotion & Sentiment Analyzer
Overview
This is a text-based sentiment and emotion analysis tool built using Streamlit and NLTK. The application allows users to upload a .txt file, processes the text for sentiment analysis, and extracts emotions.

Features
Sentiment Analysis: Determines whether the uploaded text expresses Positive, Negative, or Neutral sentiment.
Emotion Detection: Identifies and counts various emotions from the text using an emotion lexicon (emotions.txt).
Visualization: Displays a bar chart representing the frequency of each emotion detected in the text.
Prerequisites
To run this project locally, ensure the following are installed:

Python 3.x
Streamlit: For building the interactive web interface.
NLTK: Natural Language Toolkit, used for text processing and analysis.
Matplotlib: For plotting the bar chart of detected emotions.
Install Dependencies
Install the necessary Python libraries using the following command:

bash
pip install streamlit nltk matplotlib
Setup Instructions
Step 1: Download NLTK Data
The following NLTK data files are required:

punkt (for tokenization)
stopwords (to filter out common stopwords)
vader_lexicon (for sentiment analysis)
wordnet (for lemmatization)
These files will be automatically downloaded when you run the app, provided you have internet access.

Step 2: Create the emotions.txt File
Create a file named emotions.txt in the same directory as your Python script. It should contain words and their associated emotions in the following format:

Makefile
happy:joy
sad:sorrow
angry:anger
excited:joy
fear:fear
Step 3: Run the Application
Launch the application by running the following command in your terminal:

bash
streamlit run app.py
This will open the Streamlit app in your default web browser.

How It Works
Upload Text File: Click the "Upload a .txt file" button to upload a .txt file containing the text you want to analyze.
Sentiment Analysis: The app uses the VADER Sentiment Analyzer to classify the text as Positive, Negative, or Neutral.
Emotion Detection: The app compares lemmatized words from the text with those in the emotions.txt file. Matches are recorded and counted.
Results:
The sentiment of the text (Positive, Negative, or Neutral) is displayed.
A list of detected emotions with their frequencies is shown.
A bar chart visualizing the frequencies of each emotion is generated.
Example
Sample emotions.txt File:
Makefile
happy:joy
sad:sorrow
angry:anger
excited:joy
fear:fear
Sample Output:
For a .txt file containing the sentence:

Code
"I feel so happy and excited today, but also a little sad."
The results might be:

Sentiment: Neutral
Emotions Detected:
joy: 2
sorrow: 1
A bar chart will also be generated showing the frequency of each emotion.
