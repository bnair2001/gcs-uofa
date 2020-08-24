from textblob import TextBlob

sentence = input("Enter sentence:")
analysis = TextBlob(sentence)
print(analysis.sentiment)
polar = analysis.sentiment.polarity
print(polar)
