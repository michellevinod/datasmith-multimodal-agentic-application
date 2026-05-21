from faster_whisper import WhisperModel


model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path):

    segments, info = model.transcribe(
        audio_path
    )

    transcript = ""

    for segment in segments:

        transcript += segment.text + " "

    duration = round(info.duration, 2)

    return {
        "transcript": transcript,
        "duration": duration
    }