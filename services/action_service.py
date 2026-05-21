def extract_action_items(text):

    lines = text.splitlines()

    action_items = []

    keywords = [
        "complete",
        "submit",
        "send",
        "finish",
        "prepare",
        "schedule",
        "update",
        "call",
        "review"
    ]

    for line in lines:

        lower_line = line.lower()

        for keyword in keywords:

            if keyword in lower_line:

                action_items.append(
                    line.strip()
                )

                break

    if len(action_items) == 0:

        return [
            "No clear action items found."
        ]

    return action_items