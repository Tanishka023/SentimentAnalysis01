

```markdown
# 📊 Text Emotion & Sentiment Analyzer

This is a **Streamlit-based web application** that performs **sentiment analysis** and **emotion detection** on uploaded `.txt` files using **Natural Language Processing (NLP)** techniques. It identifies the overall sentiment of the text as **positive**, **negative**, or **neutral**, and extracts specific **emotions** like joy, anger, sadness, etc., which are then visualized as a bar chart.

---

## 🧠 Project Overview

This application enables quick, interactive analysis of textual content to:
- Determine **sentiment polarity** using the **VADER Sentiment Analyzer**.
- Detect **emotions** by matching words to a curated **emotion lexicon** (`emotions.txt`).
- Provide a **visual summary** of emotions using a **bar graph**.

It is particularly useful for analyzing customer reviews, social media posts, personal writings, and more.

---

## 🛠️ Tech Stack & Tools Used

| Tool / Library | Purpose |
|----------------|---------|
| **Python 3** | Core language for development |
| **Streamlit** | Web framework for building interactive ML/NLP apps |
| **NLTK (Natural Language Toolkit)** | Used for tokenization, stopword removal, lemmatization, and sentiment analysis |
| **VADER (Valence Aware Dictionary and sEntiment Reasoner)** | Pre-trained sentiment analysis model from NLTK |
| **Matplotlib** | Visualization library to display emotion frequency as a bar chart |
| **Custom Lexicon** | `emotions.txt` maps specific words to emotion labels |

---

## 🔧 NLP Workflow

1. **Text Preprocessing**:
   - Convert to lowercase
   - Remove punctuation
   - Tokenize text using `word_tokenize()`
   - Remove stopwords using NLTK's English stopwords
   - Lemmatize tokens using `WordNetLemmatizer`

2. **Emotion Extraction**:
   - Read the `emotions.txt` file (word:emotion format)
   - Match lemmatized words to emotion keywords
   - Count occurrences using `collections.Counter`

3. **Sentiment Analysis**:
   - Run VADER's `SentimentIntensityAnalyzer` on the cleaned text
   - Classify based on compound polarity scores

4. **Visualization**:
   - Display emotions as a bar chart using Matplotlib
   - Output sentiment as text summary in the Streamlit UI


## 🚀 Installation & Running

### 🔗 Clone the repository
```bash
git clone https://github.com/your-username/SentimentAnalysis01.git
cd SentimentAnalysis01
````

### 📦 Install required packages

```bash
pip install -r requirements.txt
```

### ▶️ Run the Streamlit app

```bash
streamlit run app.py
```

### 📂 Upload a `.txt` file through the interface and get results instantly.

---

## 📑 Sample emotions.txt Format

```
happy:joy
sad:sadness
angry:anger
afraid:fear
surprised:surprise
trusting:trust
```

You can customize this file to extend the app’s emotion detection vocabulary.

---

## ✅ Example Output

* **Sentiment**: Positive Sentiment
* **Emotions**:

  ```json
  {
    "joy": 3,
    "trust": 2,
    "surprise": 1
  }
  ```
* **Bar Chart**: Visual representation of the emotion distribution.

---

## 📦 requirements.txt

```
streamlit
matplotlib
nltk
```

---

## 💡 Future Enhancements

* Live text input instead of file upload
* Word cloud visualization of top words/emotions
* Support for multiple languages
* Integration with Twitter or email for real-time sentiment checks

---

## 🙋‍♀️ Author

**Tanishka023**
📎 GitHub: [Tanishka023](https://github.com/Tanishka023)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

```

---

Let me know if you'd like me to save this as a file or push it to your repo structure.
```
