def analyze_sentiment(text):

    positive = ["success","growth","good","win","positive","benefit"]
    negative = ["war","loss","crisis","fail","decline","problem"]

    text = text.lower()

    score = 0

    for word in positive:
        if word in text:
            score += 1

    for word in negative:
        if word in text:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"