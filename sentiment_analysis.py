from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text using TextBlob.

    Args:
    - text (str): The text to analyze.

    Returns:
    - str: "positive", "neutral", or "negative" based on the sentiment.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

if __name__ == "__main__":
    sample_text = "I love this stock!"
    sentiment = analyze_sentiment(sample_text)
    print(f"The sentiment of the text is: {sentiment}")
