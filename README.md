

---

````markdown
# 📊 Text Emotion & Sentiment Analyzer

This is a Streamlit web application that analyzes the **sentiment** and **emotions** in a given `.txt` file using Natural Language Processing (NLP). It identifies whether the sentiment of the text is **positive**, **negative**, or **neutral**, and visualizes detected emotions with a bar chart.

---

## 🔍 Features

- ✅ Upload any `.txt` file for analysis.
- 🧠 Performs sentiment analysis using **VADER** from NLTK.
- 😊 Detects emotions based on keywords using a custom `emotions.txt` file.
- 📊 Displays emotion distribution as a bar chart using Matplotlib.
- 🚫 Removes stopwords and punctuation.
- 🌐 Runs on **Streamlit**, deployable to the web easily.

---

## 🧪 Example Output

- **Sentiment:** Positive Sentiment  
- **Emotions:**  
  ```json
  {
    "joy": 3,
    "trust": 2,
    "surprise": 1
  }
````

* **Bar Chart:**
  Emotion distribution displayed using Matplotlib.

---

## 📁 Project Structure

```
SentimentAnalysis01/
├── app.py                # Main Streamlit app
├── emotions.txt          # Keyword-to-emotion mappings
├── read.txt              # Sample input file
├── requirements.txt      # Python dependencies
├── nltk_data/            # Auto-created directory for NLTK resources
├── README.md             # Project documentation
```

---

## 🧠 How It Works

1. The uploaded text is cleaned (lowercased, punctuation removed).
2. Tokenized and filtered using NLTK's stopwords.
3. Lemmatized using WordNetLemmatizer.
4. Each word is matched with entries in `emotions.txt`.
5. VADER sentiment analyzer calculates polarity.
6. Results (sentiment + emotion distribution) are displayed.

---

## 🚀 Installation & Usage

### ⚙️ Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/SentimentAnalysis01.git
cd SentimentAnalysis01
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

4. **Upload a `.txt` file** in the interface and view the results.

---

### 🧩 Required NLTK Resources

These will be automatically downloaded:

* `punkt`
* `stopwords`
* `vader_lexicon`
* `wordnet`

No manual steps required.

---

## 📦 requirements.txt

```
streamlit
matplotlib
nltk
```

---

## 📑 Sample emotions.txt Format

```
happy:joy
sad:sadness
angry:anger
trusting:trust
afraid:fear
```

---

## 💡 Future Improvements

* Add support for multi-language emotion detection.
* Enhance visualizations (e.g., pie charts or word clouds).
* Add real-time text input instead of file upload.

---

## 🙋‍♀️ Author

**Tanishka023**
Feel free to connect on [GitHub](https://github.com/Tanishka023)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

```

---

Would you like this saved as `README.md` and added to your project automatically?
```
