from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hehe Bwoii"}

@router.get("/hehe/{name}")
async def say_my_name(name: str):
    return {"message": f"{name}. You're Goddamn Right."}

