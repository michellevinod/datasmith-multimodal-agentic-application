def detect_intent(message):

    msg = message.lower()

    if (
        "youtube.com" in msg
        or "youtu.be" in msg
    ):
        return "youtube_transcript"

    if "summarize" in msg:
        return "summarize"

    if "summary" in msg:
        return "summarize"

    if "sentiment" in msg:
        return "sentiment"

    if "explain" in msg:
        return "code_explanation"

    if "what are the action items" in msg:
        return "action_items"

    if "sentiment" in msg:
        return "sentiment"

    return "unknown"