## 📘 News Article Summarizer using Python (NLP + Tkinter)

### 📌 Project Overview

This project is a News Article Summarization Application built using Natural Language Processing (NLP) and Machine Learning techniques.

This project is a News Article Summarizer built using:
 - Tkinter (Python GUI)
 - Newspaper3k (Extracts news article text)
 - NLTK
 - TextBlob (Sentiment Analysis)

The user enters a news URL, and the application automatically:

- ✔ Extracts the article
- ✔ Fetches the title, author, publish date
- ✔ Generates a summary
- ✔ Performs sentiment analysis

![imagealt](https://github.com/Sujithandra/Summarize_News_Article/blob/a610a6bec9de10d1696f76a9407b38de61fd14cb/output_img/WhatsApp%20Image%202025-11-20%20at%2000.08.03.jpeg)

## 🧠 How the System Works (Step-by-Step Workflow)
1️. User enters a news URL

The URL is taken from the Tkinter textbox.

2️. Article is downloaded

Article.download() fetches the content from the website.

3️. HTML is parsed

Article.parse() extracts:
- Title
- Author
- Publish date
- Main article text

4️. NLP techniques are applied

- Article.nlp() performs:
- Sentence tokenization
- Keyword extraction
- Automatic summarization (TextRank Algorithm)

5️. Sentiment analysis is performed

- Using TextBlob, the app calculates:
- The polarity (from –1 to +1)
- Determines if the article is:
- Positive
- Negative
- Neutral

6️. Results are displayed in GUI

- All results appear in organized sections:
- Title
- Author
- Publish Date
- Summary
- Sentiment

------------

## 🧰 Detailed Explanation of Every Module Used

1. Tkinter — GUI Framework

     Tkinter is Python’s inbuilt library for building Graphical User Interfaces.

Purpose in Project

- Create window layout
- Display labels, text boxes, and output areas
- Add the "Summarize" button
- Handle user events

2. NLTK — Natural Language Toolkit

NLTK is the most widely used toolkit for Linguistic and NLP operations.

Why We Use It

- Tokenization
- Sentence splitting
- Language modeling support

3. TextBlob — Sentiment Analysis

   TextBlob is a simple library built on top of NLTK that allows easy sentiment analysis.

   analysis = TextBlob(article.text)
   polarity = analysis.polarity

--------------

## 🎯 Features of the Application
- ✔ Fetches complete article from any news URL
- ✔ Auto-generates summary using NLP (TextRank)
- ✔ Performs sentiment analysis
- ✔ Clean and simple GUI
- ✔ Error-free and fast processing

## 📂 Folder Structure
news-summarizer

│── README.md

│── app.py

│── requirements.txt

└── screenshots

    └── sample_output.png

-------------

## 📌 Summary

This project is a fully automated News Summarizer that combines:

- Web scraping
- Natural language processing
- Machine learning
- Sentiment analysis
- GUI development

It demonstrates the powerful combination of Python + NLP to convert any long article into a short, meaningful summary instantly.


## 📦 Installation & Setup

1️⃣ Install dependencies

- pip install newspaper3k

- pip install textblob

- pip install nltk

2️⃣ Download NLTK tokenizer

- import nltk

- nltk.download("punkt")

3️⃣ Run the app

- python app.py



