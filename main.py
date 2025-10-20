from fastapi import APIRouter, FastAPI
from api import API
import uvicorn

app = FastAPI()
router = APIRouter()
api = API()

router.include_router(api.router)

app.include_router(router, prefix='/book_ai')

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True

    )


