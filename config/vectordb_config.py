from chromadb import Client
from chromadb.config import Settings

# Collection name
FRONTEND_OPERATION_COLLECTION = "frontend_operation"


def get_client() -> Client:
    return Client(
        Settings(chroma_db_impl="duckdb+parquet", persist_directory="./vectordb")
    )
