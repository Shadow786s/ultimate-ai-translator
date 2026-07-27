import re

from typing import List

from .schemas import SubtitleEntry


TIME_PATTERN = re.compile(
    r"(\d{2}:\d{2}:\d{2},\d{3})"
    r"\s*-->\s*"
    r"(\d{2}:\d{2}:\d{2},\d{3})"
)


def parse_srt(
    content: str
) -> List[SubtitleEntry]:

    content = content.replace(
        "\r\n",
        "\n"
    )

    content = content.replace(
        "\r",
        "\n"
    )

    blocks = re.split(
        r"\n\s*\n",
        content.strip()
    )

    entries = []

    for block in blocks:

        lines = block.split("\n")

        if len(lines) < 3:
            continue

        try:

            index = int(
                lines[0].strip()
            )

        except ValueError:

            continue

        match = TIME_PATTERN.match(
            lines[1].strip()
        )

        if not match:
            continue

        start = match.group(1)

        end = match.group(2)

        text = "\n".join(
            lines[2:]
        ).strip()

        entries.append(
            SubtitleEntry(
                index=index,
                start=start,
                end=end,
                text=text
            )
        )

    return entries
