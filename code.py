import tkinter as tkinter
import nltk
from textblob import textblob
from newspaper import Article

def summarize():
    url= utext.get('1.0',"end").strip()
    articl=Articl(url)

    article=.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0', article.title)

    author.delete('1.0','end')
    author.insert('1.0', article.authors)

    publication.delete('1.0','end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0', article.summary)

    analysis=TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'polarity:{analysis.polarity}, sentiment: {"postive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
    
    title.config(state='disable')
    author.config(state='disable')
    publication.config(state='disable')
    summary.config(state='normal')
    sentiment.config(state='disable')


root=tk.Tk()
root.title("News Sumarizer")
root.geometry("1200*600")

tlabel= tk.label(root, text="Title")
tlabel.pack()

tlabel= tk.label(root, height=1, width=140 )
title.config(stste='disabled', bg="red")
title.pack()


alabel= tk.label(root, text="Author")
alabel.pack()

author= tk.label(root, height=1, width=140 )
author.config(stste='disabled', bg="blue")
author.pack()

plabel= tk.label(root, text="Publish date")
plabel.pack()

publication= tk.label(root, height=1, width=140 )
publication.config(stste='disabled', bg="orange")
publication.pack()

slabel= tk.label(root, text="Summary")
slabel.pack()

summary= tk.label(root, height=1, width=140 )
summary.config(stste='disabled', bg="yellow")
summary.pack()

selabel= tk.label(root, text="sentiment analysis")
selabel.pack()

sentiment= tk.label(root, height=1, width=140 )
sentiment.config(stste='disabled', bg="pink")
sentiment.pack()

ulabel= tk.label(root,height=1,width=140)
utext.pack()

btn-tk.Button(root, text="summarize" command=summarize)
btn.pack()

root.mainloop()

