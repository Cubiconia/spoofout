import uvicorn
import os

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv(dotenv_path=".env")

    uvicorn.run(
        "main:app",
        host=os.environ["HOST"] or "127.0.0.1",
        port=int(os.environ["PORT"]) or 7901,
        reload=False,
        log_level="info"
    )
