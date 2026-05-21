from youtube_transcript_api import (
    YouTubeTranscriptApi
)

import re


def extract_video_id(url):

    patterns = [

        r"v=([0-9A-Za-z_-]{11})",

        r"youtu\\.be/([0-9A-Za-z_-]{11})",

        r"shorts/([0-9A-Za-z_-]{11})"
    ]

    for pattern in patterns:

        match = re.search(pattern, url)

        if match:
            return match.group(1)

    return None


def get_youtube_transcript(url):

    video_id = extract_video_id(url)

    if not video_id:
        return "Invalid YouTube URL"

    try:

        transcript = (
            YouTubeTranscriptApi
            .fetch(video_id)
        )

        text = ""

        for item in transcript:

            text += item.text + " "

        return text

    except Exception as e:

        print("Transcript error:", e)

        return (
            "Transcript unavailable for this video."
        )