from textblob import TextBlob 

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity

    if polarity > 0:
        sentiment_category = "Positive :-)"
    elif polarity <0:
        sentiment_category = "negative :("
    else:
        sentiment_category = "netural"  
    
    return sentiment_category

text= input ("enter the text you want")
result = analyze_sentiment(text)
print(f"sentiment:{result}")