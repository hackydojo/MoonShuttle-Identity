from fastapi import APIRouter, Depends, HTTPException, Request

router = APIRouter()


# -----------------------------------------------------------------------------
# GET /
# -----------------------------------------------------------------------------
@router.get('/', tags=['v1'])
async def get_root(request: Request):
    return {
        'message': 'MoonShuttle Project Template',
        'client_host': request.client.host,
        'system_status': 'UP'
    }
