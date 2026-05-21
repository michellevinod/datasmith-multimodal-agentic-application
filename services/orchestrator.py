from services.intent_service import detect_intent
from services.summary_service import summarize_text
from services.youtube_service import (
    get_youtube_transcript
)
from services.sentiment_service import (
    analyze_sentiment
)
from services.code_service import explain_code
from services.action_service import (
    extract_action_items
)



def process_request(message, extracted_text):

    intent = detect_intent(message)

    execution_logs = []

    execution_logs.append(
        f"Detected intent: {intent}"
    )

    if intent == "unknown":

        return {
            "response":
            "Could you clarify what you want me to do with this content?",
            "logs": execution_logs
        }

    if intent == "summarize":

        execution_logs.append(
            "Running summarization pipeline"
        )

        summary = summarize_text(extracted_text)

        return {
            "response": summary,
            "logs": execution_logs
        }

    if intent == "youtube_transcript":

        execution_logs.append(
            "Fetching YouTube transcript"
        )

        transcript = get_youtube_transcript(
            message
        )

        summary = summarize_text(transcript)

        return {
            "response": summary,
            "logs": execution_logs
        }

    if intent == "sentiment":

        execution_logs.append(
            "Running sentiment analysis"
        )

        sentiment = analyze_sentiment(
            extracted_text or message
        )

        return {
            "response": sentiment,
            "logs": execution_logs
        }

    if intent == "code_explanation":

        execution_logs.append(
            "Running code explanation"
        )

        result = explain_code(
            extracted_text
        )

        return {
            "response": result,
            "logs": execution_logs
        }

    if intent == "action_items":

        execution_logs.append(
            "Extracting action items"
        )

        actions = extract_action_items(
            extracted_text
        )

        return {
            "response": actions,
            "logs": execution_logs
        }


    return {
        "response":
        f"Task identified successfully: {intent}",
        "logs": execution_logs
    }