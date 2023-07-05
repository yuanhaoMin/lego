from config.api_config import get_openai_key
from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseMessage, HumanMessage


def completion(messages: list[BaseMessage]):
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=get_openai_key(),
        request_timeout=30,
    )
    ai_message = llm(messages)
    return ai_message.content
