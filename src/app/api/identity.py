from fastapi import APIRouter, Depends, HTTPException, Request

router = APIRouter()


@router.post('/identity', tags=["v1"])
def create_identity():
    return {"msg": "not implemented"}