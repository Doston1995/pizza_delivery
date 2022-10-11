from fastapi import APIRouter


router = APIRouter()


@router.get('')
async def order():
    return {'message':"Order page"}