from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from app.services.parser import (
    SRTParser
)

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
            detail="Only SRT files are supported."
        )

    data = await file.read()

    if len(data) == 0:

        raise HTTPException(
            status_code=400,
            detail="Empty file."
        )

    try:

        text = SRTParser.decode_file(data)

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Subtitle encoding not supported."
        )

    subtitles = SRTParser.parse(text)

    if len(subtitles) == 0:

        raise HTTPException(
            status_code=400,
            detail="Invalid SRT file."
        )

    return {

        "success": True,

        "filename": file.filename,

        "subtitle_count": len(subtitles),

        "status": "uploaded"

    }
