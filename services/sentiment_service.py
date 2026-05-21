def analyze_sentiment(text):

    text_lower = text.lower()

    positive_words = [
        "good",
        "great",
        "excellent",
        "happy",
        "love",
        "amazing",
        "success",
        "excited",
        "awesome",
        "positive"
    ]

    negative_words = [
        "bad",
        "terrible",
        "sad",
        "hate",
        "angry",
        "failure",
        "poor",
        "worst",
        "negative",
        "upset"
    ]

    positive_score = 0
    negative_score = 0

    for word in positive_words:

        if word in text_lower:

            positive_score += 1

    for word in negative_words:

        if word in text_lower:

            negative_score += 1


    # Positive Sentiment

    if positive_score > negative_score:

        label = "Positive"

        confidence = "85%"

        reason = (
            "The text contains more "
            "positive and optimistic words."
        )


    # Negative Sentiment

    elif negative_score > positive_score:

        label = "Negative"

        confidence = "85%"

        reason = (
            "The text contains more "
            "negative or critical words."
        )


    # Neutral Sentiment

    else:

        label = "Neutral"

        confidence = "70%"

        reason = (
            "No strong positive or "
            "negative sentiment detected."
        )


    return f"""
Sentiment Analysis
-------------------

Label:
{label}

Confidence:
{confidence}

Justification:
{reason}
"""