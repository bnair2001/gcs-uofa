from textblob import TextBlob

sentence = input("Enter sentence:")
analysis = TextBlob(sentence)

polar = analysis.sentiment.polarity
print(polar)