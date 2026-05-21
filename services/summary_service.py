import re


def summarize_text(text):

    if not text.strip():

        return "No text found."


    # Clean text

    cleaned_text = re.sub(
        r'\s+',
        ' ',
        text
    ).strip()


    # Split sentences better

    sentences = re.split(
        r'(?<=[.!?])\s+',
        cleaned_text
    )


    # Remove tiny garbage lines

    filtered_sentences = []

    for sentence in sentences:

        if len(sentence.strip()) > 25:

            filtered_sentences.append(
                sentence.strip()
            )


    if len(filtered_sentences) == 0:

        return "Unable to generate summary."


    # 1-line summary

    one_line = filtered_sentences[0]


    # Bullet points

    bullet_points = []

    for sentence in filtered_sentences[1:4]:

        bullet_points.append(
            f"• {sentence}"
        )


    # 5-sentence summary

    five_sentence_summary = ". ".join(
        filtered_sentences[:5]
    )


    return f"""
1-Line Summary
-------------------

{one_line}


3 Key Points
-------------------

{chr(10).join(bullet_points)}


5-Sentence Summary
-------------------

{five_sentence_summary}
"""