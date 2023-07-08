import logging
from config.api_config import get_openai_key
from fastapi import HTTPException
from langchain.chat_models import openai
from langchain.schema import BaseMessage
from openai import ChatCompletion

logger = logging.getLogger(__name__)


def completion(messages: list[BaseMessage]):
    message_dicts = [openai._convert_message_to_dict(m) for m in messages]
    contents = []
    retry_count = 0
    max_retries = 2
    while True:
        try:
            response = ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=message_dicts,
                request_timeout=2,
                temperature=0,
                stream=True,
            )
            for stream_response in response:
                delta = stream_response["choices"][0]["delta"]
                finish_reason = stream_response["choices"][0]["finish_reason"]
                if hasattr(delta, "content"):
                    contents.append(delta.content)
                if finish_reason == "stop":
                    full_response_text = "".join(contents)
            return full_response_text
        except Exception as e:
            retry_count += 1
            if retry_count > max_retries:
                raise HTTPException(
                    status_code=504,
                    detail=f"Failed to get response from OpenAI API after {max_retries} retries. Error: {e}",
                )
            else:
                logger.warning("Failed to get response from OpenAI API. Retrying...")
                continue
