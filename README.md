<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Emotion & Sentiment Analyzer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }
        section {
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
        pre {
            background-color: #eee;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        ul {
            list-style-type: none;
        }
        li {
            padding: 5px 0;
        }
        .important {
            color: red;
            font-weight: bold;
        }
        footer {
            background-color: #333;
            color: #fff;
            padding: 1rem;
            text-align: center;
            position: absolute;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>

<header>
    <h1>Text Emotion & Sentiment Analyzer</h1>
    <p>A Streamlit web application to analyze emotions and sentiments in text files.</p>
</header>

<section>
    <h2>Project Overview</h2>
    <p>This project is a web application developed using <strong>Streamlit</strong> that allows users to upload a text file. It then processes the text to detect emotions and perform sentiment analysis using the <strong>NLTK</strong> library.</p>

    <h2>Features</h2>
    <ul>
        <li>Text Emotion Detection</li>
        <li>Sentiment Analysis (Positive, Negative, Neutral)</li>
        <li>Visual representation of detected emotions in a bar chart</li>
    </ul>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Streamlit</strong> - Web app framework for building the user interface</li>
        <li><strong>NLTK</strong> - Natural Language Toolkit for text processing</li>
        <li><strong>Matplotlib</strong> - For visualizing the emotions detected in the text</li>
    </ul>

    <h2>How to Use</h2>
    <ol>
        <li>Clone the repository to your local machine.</li>
        <li>Install the required dependencies by running:
            <pre>pip install -r requirements.txt</pre>
        </li>
        <li>Run the Streamlit application using:
            <pre>streamlit run app.py</pre>
        </li>
        <li>Upload a text file using the uploader in the web app.</li>
        <li>View the detected emotions and sentiment analysis results.</li>
    </ol>

    <h2>Code Overview</h2>
    <p>The <code>app.py</code> script is the main entry point of the application. It utilizes <strong>NLTK</strong> for text processing, including tokenization, lemmatization, stopword removal, and sentiment analysis.</p>

    <h3>Example Code Snippet</h3>
    <pre>
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

# Function to process text
def process_text(text):
    # Text processing steps
    pass
    </pre>

    <h2>Emotions File</h2>
    <p>The emotions file <code>emotions.txt</code> contains a list of words mapped to emotions. For example:</p>
    <pre>happy:joy</pre>
    <p>The analyzer checks if words from the uploaded text match any in this file to detect emotions.</p>

    <h2>Important Notes</h2>
    <p class="important">Make sure the <code>emotions.txt</code> file is in the same directory as the application for emotion detection to work properly.</p>

    <h2>Getting Started</h2>
    <ol>
        <li>Download or clone the repository from GitHub.</li>
        <li>Install dependencies: <pre>pip install -r requirements.txt</pre></li>
        <li>Run the application: <pre>streamlit run app.py</pre></li>
    </ol>

</section>

<footer>
    <p>&copy; 2025 Text Emotion & Sentiment Analyzer. All Rights Reserved.</p>
</footer>

</body>
</html>

