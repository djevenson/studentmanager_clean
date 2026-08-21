import os
from dotenv import load_dotenv

load_dotenv()

def build_db_connection_string() -> str:
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    return (
        f"dbname={db_name} user={db_user} password={db_password} "
        f"host={db_host} port={db_port}"
    )