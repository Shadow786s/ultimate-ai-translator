import re
from typing import List, Dict

SRT_PATTERN = re.compile(
    r"(\d+)\s*\n"
    r"(\d{2}:\d{2}:\d{2},\d{3})\s-->\s(\d{2}:\d{2}:\d{2},\d{3})\s*\n"
    r"(.*?)(?=\n{2,}|\Z)",
    re.DOTALL,
)


class SRTParser:

    @staticmethod
    def decode_file(data: bytes) -> str:

        encodings = [
            "utf-8",
            "utf-8-sig",
            "utf-16",
            "utf-16-le",
            "utf-16-be",
            "cp1252",
            "latin-1",
        ]

        for encoding in encodings:

            try:
                return data.decode(encoding)

            except UnicodeDecodeError:
                continue

        raise ValueError(
            "Unsupported subtitle encoding."
        )

    @staticmethod
    def parse(text: str) -> List[Dict]:

        subtitles = []

        matches = SRT_PATTERN.findall(text)

        for match in matches:

            subtitles.append({

                "index": int(match[0]),

                "start": match[1],

                "end": match[2],

                "text": match[3].strip()

            })

        return subtitles

    @staticmethod
    def total(subtitles: List[Dict]) -> int:

        return len(subtitles)
