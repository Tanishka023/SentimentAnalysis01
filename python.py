import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import nltk

# Download necessary NLTK data files
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')

# Read and preprocess text
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
clean_text = lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_words = word_tokenize(clean_text, "english")

# Remove stopwords
final_words = [word for word in tokenized_words if word not in stopwords.words('english')]

# Emotion analysis
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

# Count emotions
w = Counter(emotion_list)
print(w)

# Sentiment analysis
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative")
    elif pos > neg:
        print("Positive")
    else:
        print("Neutral")

# Call sentiment analysis
sentiment_analyse(clean_text)

# Plotting the emotion counts
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
