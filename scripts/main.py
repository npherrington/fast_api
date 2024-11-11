from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Router
router = APIRouter()

class MyRequest(BaseModel):
    some_name: str

@router.post("/my_endpoint")
async def my_endpoint(request: MyRequest) -> str:
    return f"blah, {request.some_name}"

# Router 2
router_two = APIRouter()

class MyRequest(BaseModel):
    some_name: str

@router_two.post("/my_endpoint")
async def my_endpoint(request: MyRequest) -> str:
    return f"blah, {request.some_name}"

# API app
api_app = FastAPI()
api_app.include_router(router, prefix="/a")
api_app.include_router(router_two, prefix="/b")

# Main app
app = FastAPI()
app.mount("/api", api_app)

@app.get("/{x}")
async def home_page(x: int) -> str:
    return f"yo {x}"

# Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)