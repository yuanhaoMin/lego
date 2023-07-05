import requests
from config.api_config import get_openai_key
from fastapi import APIRouter, UploadFile
from util.data_utils import convert_traditional_to_simplified, replace_keywords

router = APIRouter(
    prefix="/audio",
    tags=["audio"],
)


@router.post("/openai/transcription")
async def openai_audio_transcribe(audio_file: UploadFile):
    headers = {"Authorization": f"Bearer {get_openai_key()}"}
    prompt = """"The scenario is industrie. Following words are common: 围栏, 巡检'"
    """
    response = requests.post(
        "https://api.openai.com/v1/audio/transcriptions",
        data={
            "language": "zh",
            "model": "whisper-1",
            "prompt": prompt,
        },
        headers=headers,
        files={
            "file": (audio_file.filename, await audio_file.read()),
        },
    )
    response_data = response.json()
    transcription_text = response_data["text"]
    simplified_text = convert_traditional_to_simplified(transcription_text)
    final_text = replace_keywords(simplified_text)
    return {"text": final_text}
