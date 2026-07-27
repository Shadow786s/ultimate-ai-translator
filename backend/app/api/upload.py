from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
from app.services.srt_service import parse_srt

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_srt(
    file: UploadFile = File(...)
):

    if not file.filename.lower().endswith(".srt"):
        raise HTTPException(
            status_code=400,
            detail="Only SRT files are allowed."
        )

    content = await file.read()

    try:

        text = content.decode("utf-8")

    except UnicodeDecodeError:

        try:

            text = content.decode("utf-16")

        except:

            try:

                text = content.decode("latin-1")

            except:

                raise HTTPException(
                    status_code=400,
                    detail="Unable to decode subtitle."
                )

    subtitles = parse_srt(text)

    if len(subtitles) == 0:

        raise HTTPException(
            status_code=400,
            detail="No subtitles found."
        )

    return {

        "job_id": str(uuid4()),

        "filename": file.filename,

        "total_subtitles": len(subtitles),

        "status": "uploaded"

    }
