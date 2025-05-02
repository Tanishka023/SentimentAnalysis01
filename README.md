<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Emotion & Sentiment Analyzer</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f7f7f7;
            color: #333;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 20px 0;
            text-align: center;
        }
        header h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        .content {
            padding: 20px;
        }
        .section-title {
            color: #333;
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        .section-content {
            margin-bottom: 20px;
            font-size: 1rem;
            line-height: 1.8;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin: 5px 0;
        }
        code {
            background-color: #f0f0f0;
            padding: 4px 8px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
        }
        pre {
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
        }
        footer {
            background-color: #333;
            color: #fff;
            padding: 15px 0;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>

<header>
    <h1>Text Emotion & Sentiment Analyzer</h1>
    <p>A Streamlit web app to detect emotions and analyze sentiment from text files.</p>
</header>

<div class="content">
    <div>
        <div class="section-title">Project Overview</div>
        <div class="section-content">
            This web application is built with <strong>Streamlit</strong> to upload a text file, analyze emotions, and perform sentiment analysis using <strong>NLTK</strong> library. The application is designed to help users detect emotions and sentiment from written text efficiently.
        </div>
    </div>

    <div>
        <div class="section-title">Features</div>
        <div class="section-content">
            <ul>
                <li>Text emotion detection based on predefined emotion-word mappings.</li>
                <li>Sentiment analysis (positive, negative, or neutral).</li>
                <li>Visual representation of detected emotions in a bar chart.</li>
            </ul>
        </div>
    </div>

    <div>
        <div class="section-title">Technologies Used</div>
        <div class="section-content">
            <ul>
                <li><strong>Streamlit</strong> - For building the web app interface.</li>
                <li><strong>NLTK</strong> - For processing the text (tokenization, sentiment analysis, lemmatization).</li>
                <li><strong>Matplotlib</strong> - For plotting detected emotions in a bar chart.</li>
            </ul>
        </div>
    </div>

    <div>
        <div class="section-title">How to Use</div>
        <div class="section-content">
            <ol>
                <li>Clone the repository.</li>
                <li>Install required dependencies: <code>pip install -r requirements.txt</code></li>
                <li>Run the Streamlit app: <code>streamlit run app.py</code></li>
                <li>Upload a text file to analyze.</li>
                <li>View the emotions and sentiment analysis results.</li>
            </ol>
        </div>
    </div>

    <div>
        <div class="section-title">Code Example</div>
        <div class="section-content">
            Below is a simplified version of the core logic for processing text and analyzing sentiment:

            <pre>
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

def process_text(text):
    cleaned_text = text.lower()
    tokenized_words = word_tokenize(cleaned_text)
    stop_words = set(stopwords.words('english'))
    final_words = [word for word in tokenized_words if word not in stop_words]

    score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    sentiment = "Positive" if score['pos'] > score['neg'] else "Negative"

    return sentiment
            </pre>
        </div>
    </div>

    <div>
        <div class="section-title">Emotions File</div>
        <div class="section-content">
            The <code>emotions.txt</code> file contains words linked to specific emotions, and the application checks the uploaded text for these words. Here's an example of how an entry in the file looks:

            <pre>happy:joy</pre>
        </div>
    </div>
</div>

<footer>
    <p>&copy; 2025 Text Emotion & Sentiment Analyzer. All Rights Reserved.</p>
</footer>

</body>
</html>

