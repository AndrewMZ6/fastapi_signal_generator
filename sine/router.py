from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def index():
    return "Hello from sine"