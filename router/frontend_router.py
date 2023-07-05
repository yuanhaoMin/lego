from config.vectordb_config import get_client
from chromadb import Client
from constant.frontend_operation_enum import EMPTY_OPERATION
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from service import frontend_service
from typing import Optional

router = APIRouter(
    prefix="/frontend",
    tags=["frontend"],
)


class DetermineFunctionRequest(BaseModel):
    operation_text: str = Field(min_length=1)
    last_operation: Optional[str] = EMPTY_OPERATION
    require_param: Optional[bool] = False


@router.post("/operation/function")
async def determine_function(
    request: DetermineFunctionRequest, client: Client = Depends(get_client)
):
    return frontend_service.determine_function(
        request.operation_text, request.last_operation, request.require_param, client
    )
