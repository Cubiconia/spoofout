import uvicorn
import os

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv(dotenv_path=".env")

    uvicorn.run(
        "main:app",
        host="localhost",
        port=int(os.environ["PORT"]) or 8888,
        reload=False,
        log_level="debug"
    )
