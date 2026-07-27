import json

from openai import AsyncOpenAI

from .config import settings
from .schemas import SubtitleEntry


client = AsyncOpenAI(
    api_key=settings.OPENAI_API_KEY
)


SYSTEM_PROMPT = """
You are an expert professional subtitle
localization translator.

Your task is to translate subtitle dialogue
into natural Roman Hindi / Hinglish.

The result must feel like a professional
human subtitle localization.

Important rules:

1. Preserve the complete meaning.
2. Understand context before translating.
3. Never perform mechanical word-by-word translation.
4. Use natural Roman Hindi / Hinglish.
5. Keep natural English words when Indians commonly
   use them in spoken conversation.
6. Do not unnecessarily copy the source language.
7. Preserve names of people, places and brands.
8. Preserve humor, sarcasm and emotions.
9. Preserve the intensity and intent of dialogue.
10. Do not add explanations.
11. Do not remove meaningful information.
12. Do not translate subtitle numbering.
13. Do not translate timestamps.
14. Return only the requested JSON structure.
15. Produce exactly one result for every input subtitle.

The final output must be easy for an Indian viewer
to read and understand naturally.

Target language:
Natural Roman Hindi / Hinglish.
"""


async def translate_batch(
    batch: list[SubtitleEntry],
    source_language: str = "auto"
) -> list[str]:

    payload = []

    for item in batch:

        payload.append(
            {
                "index": item.index,
                "text": item.text
            }
        )


    user_prompt = f"""
Source language:
{source_language}

Translate the following subtitles into
natural Roman Hindi / Hinglish.

Input subtitles:

{json.dumps(
    payload,
    ensure_ascii=False,
    indent=2
)}

Return ONLY JSON in this exact format:

{{
  "translations": [
    {{
      "index": 1,
      "translation": "translated text"
    }}
  ]
}}

Do not return Markdown.
Do not return explanations.
"""


    response = await client.chat.completions.create(

        model=settings.OPENAI_MODEL,

        temperature=0.2,

        response_format={
            "type": "json_object"
        },

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )


    content = (
        response
        .choices[0]
        .message
        .content
    )


    data = json.loads(
        content
    )


    results = data.get(
        "translations",
        []
    )


    result_map = {

        int(item["index"]):
        item["translation"]

        for item in results
    }


    output = []


    for item in batch:

        output.append(
            result_map.get(
                item.index,
                ""
            )
        )


    return output
