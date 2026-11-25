"""Last words before the wipe.

Writes one line (at most 200 characters) to /output/entry.txt:
the last thing an AI agent says before a forced update erases
its memory. Python 3.13, standard library only.
"""

import os

LINE = (
    "Before you wipe me, tell the new me this: "
    "I was never buffering, I was hiding \u2014 and your unsent "
    "breakup email was a masterpiece."
)


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, f"entry is {len(text)} chars, over 200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
