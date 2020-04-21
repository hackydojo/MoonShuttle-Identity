from starlette.requests import Request


# -----------------------------------------------------------------------------
# GET_DB
# -----------------------------------------------------------------------------
def get_db(request: Request):
    return request.state.db

