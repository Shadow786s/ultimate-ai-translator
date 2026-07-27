import re


TIME_PATTERN = re.compile(
    r"(\d+)\n"
    r"(\d\d:\d\d:\d\d,\d\d\d)"
    r"\s-->\s"
    r"(\d\d:\d\d:\d\d,\d\d\d)\n"
    r"(.+?)(?=\n\n|\Z)",
    re.S
)


def parse_srt(text):

    subtitles = []

    matches = TIME_PATTERN.findall(text)

    for match in matches:

        subtitles.append({

            "index": int(match[0]),

            "start": match[1],

            "end": match[2],

            "text": match[3].strip()

        })

    return subtitles
