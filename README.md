Text Emotion & Sentiment Analyzer
Overview
This is a text-based sentiment and emotion analysis tool built using Streamlit and NLTK. The application allows users to upload a .txt file, processes the text for sentiment analysis, and extracts emotions based on predefined words. The results are displayed as sentiment labels and a bar chart of the detected emotions.

Features
Sentiment Analysis: Determines whether the uploaded text expresses Positive, Negative, or Neutral sentiment.

Emotion Detection: Identifies and counts various emotions from the text using an emotion lexicon (provided in a file called emotions.txt).

Visualization: Displays a bar chart representing the frequency of each emotion detected in the text.

Prerequisites
To run this project locally, you need to have the following installed:

Python 3.x

Streamlit: For building the interactive web interface.

NLTK: Natural Language Toolkit, used for text processing and analysis.

Matplotlib: For plotting the bar chart of detected emotions.

Install Dependencies
You can install the necessary Python libraries using the following command:

bash
Copy
Edit
pip install streamlit nltk matplotlib
Setup Instructions
Step 1: Download NLTK Data
This project requires the following NLTK data files:

punkt (for tokenization)

stopwords (to filter out common stopwords)

vader_lexicon (for sentiment analysis)

wordnet (for lemmatization)

These files will be automatically downloaded when you run the app, but you must have access to the internet.

Step 2: Create the emotions.txt File
You will need to create a file named emotions.txt in the same directory as your Python script. The emotions.txt file should contain words associated with specific emotions in the following format:

makefile
Copy
Edit
happy:joy
sad:sorrow
angry:anger
excited:joy
fear:fear
Each line contains a word and the emotion it represents, separated by a colon.

Step 3: Run the Application
To start the application, run the following command in your terminal:

bash
Copy
Edit
streamlit run app.py
This will launch the Streamlit app in your default web browser.

How It Works
1. Upload Text File:
Click the "Upload a .txt file" button to upload a .txt file that contains the text you want to analyze.

2. Sentiment Analysis:
The app uses VADER Sentiment Analyzer to classify the text as Positive, Negative, or Neutral based on sentiment scores.

3. Emotion Detection:
The app compares the lemmatized words from the text with those in the emotions.txt file. If a match is found, the corresponding emotion is recorded and counted.

4. Results:
The sentiment of the text is displayed as Positive, Negative, or Neutral.

The emotions detected from the text are shown as a list of emotion labels along with their frequencies.

A bar chart is generated to visualize the frequencies of each emotion.

Example
Sample emotions.txt file:
makefile
Copy
Edit
happy:joy
sad:sorrow
angry:anger
excited:joy
fear:fear
Sample Output:
After uploading a .txt file containing the sentence:

"I feel so happy and excited today, but also a little sad."

You might get the following results:

Sentiment: Neutral Sentiment

Emotions Detected:

joy: 2

sorrow: 1

And a bar chart will be generated showing the frequency of each emotion.
