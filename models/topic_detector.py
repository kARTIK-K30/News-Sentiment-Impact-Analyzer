def detect_topic(text):

    text = text.lower()

    if "government" in text or "election" in text:
        return "Politics"

    elif "market" in text or "stock" in text:
        return "Finance"

    elif "technology" in text or "ai" in text:
        return "Technology"

    elif "sport" in text or "match" in text:
        return "Sports"

    else:
        return "General"