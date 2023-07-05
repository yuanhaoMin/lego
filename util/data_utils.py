import logging
from opencc import OpenCC

logger = logging.getLogger(__name__)


def convert_traditional_to_simplified(text):
    simplified_text = OpenCC("t2s").convert(text)
    return simplified_text


def replace_keywords(text: str):
    original_text = text
    keyword_dict = {
        "回览": "围栏",
        "维兰": "围栏",
        "蔚蓝": "围栏",
        "微软": "围栏",
        "未来": "围栏",
        "为蓝": "围栏",
        "委栏": "围栏",
        "寻检": "巡检",
        "询检": "巡检",
    }
    for key, value in keyword_dict.items():
        text = text.replace(key, value)
    if original_text != text:
        logger.warn(f"Replaced keywords: {original_text} -> {text}")
    return text
