from flask import Flask, render_template, request
import string
from collections import Counter
import matplotlib.pyplot as plt
import os

from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

app = Flask(__name__)

def process_text(text):
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    tokenized_words = word_tokenize(cleaned_text, "english")

    final_words = [word for word in tokenized_words if word not in stopwords.words('english')]

    lemma_words = [WordNetLemmatizer().lemmatize(word) for word in final_words]

    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in lemma_words:
                emotion_list.append(emotion)

    emotion_counter = Counter(emotion_list)

    score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    if score['neg'] > score['pos']:
        sentiment = "Negative Sentiment"
    elif score['neg'] < score['pos']:
        sentiment = "Positive Sentiment"
    else:
        sentiment = "Neutral Sentiment"

    return emotion_counter, sentiment

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_file = request.files['textfile']
        text = text_file.read().decode('utf-8')
        emotions, sentiment = process_text(text)

        # Plot and save the bar graph
        fig, ax1 = plt.subplots()
        ax1.bar(emotions.keys(), emotions.values())
        fig.autofmt_xdate()
        graph_path = os.path.join('static', 'graph.png')
        plt.savefig(graph_path)
        plt.close()

        return render_template('result.html', emotions=emotions, sentiment=sentiment, graph='graph.png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
