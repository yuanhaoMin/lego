from chromadb import Client
from config.vectordb_config import FRONTEND_OPERATION_COLLECTION
from constant.frontend_operation_enum import EMPTY_OPERATION, FrontendOperation
from constant.frontend_operation_param_enum import FrontendOperationParam
from fastapi import HTTPException
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import HumanMessage, SystemMessage
from util.json_utils import fix_and_parse_json
from util.openai_utils import completion


def determine_function(
    operation_text: str, last_operation: str, require_param: bool, client: Client
) -> str:
    collection = client.get_collection(FRONTEND_OPERATION_COLLECTION)
    query_embeddings = OpenAIEmbeddings().embed_documents([operation_text])
    results = collection.query(
        n_results=1,
        query_embeddings=query_embeddings,
        where={
            "$or": [
                {"parent_operation": {"$eq": EMPTY_OPERATION}},
                {"parent_operation": {"$eq": last_operation}},
            ]
        },
    )
    operation = FrontendOperationParam.find_by_function_name(results["ids"][0][0])
    if operation:
        return determine_function_and_param(operation, operation_text)
    else:
        if require_param:
            operation = FrontendOperationParam.find_by_parent_operation(last_operation)
            return determine_function_and_param(operation, operation_text)
        else:
            operation = FrontendOperation.find_by_function_name(results["ids"][0][0])
            return {"function_name": operation.function_name, "function_level": 1}


def determine_function_and_param(
    operation: FrontendOperationParam, operation_text: str
):
    # 确认或返回等简短操作
    if len(operation_text) <= 3:
        user_message_content = """
        Based on the user input, you need to decide the operation type and give a JSON output.
        For example, if the user input is '确认' or something similar to confirmation, you need to return the following JSON:
        {
            "function_name": "submit",
            "function_level": 2,
        }
        If the user input is '返回' or something similar to cancellation, you need to return the following JSON:
        {
            "function_name": "cancel",
            "function_level": 2,
        }
        But if the user input has other meanings, you need to return the following JSON:
        {
            "function_name": "unknown",
            "function_level": 2,
        }
        """
        user_message_content += "Here is the user input: " + operation_text
        parameter_json = completion([HumanMessage(content=user_message_content)])
        try:
            data = fix_and_parse_json(parameter_json)
            if data["function_name"] != "unknown":
                return data
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"Failed to parse parameters '{parameter_json}' for the operation '{operation.function_name}'",
            )
    system_message = SystemMessage(content=operation.param_prompt)
    user_message = HumanMessage(content=operation_text)
    parameter_json = completion([system_message, user_message])
    try:
        data = fix_and_parse_json(parameter_json)
        return {
            "function_name": operation.function_name,
            "data": data,
            "function_level": 2,
        }
    except Exception:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to parse parameters '{parameter_json}' for the operation '{operation.function_name}'",
        )
