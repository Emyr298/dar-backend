from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def exception_handler(request: Request, exc: Exception):
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={'message': exc.detail,}
        )
    else:
        return JSONResponse(
            status_code=500,
            content={'message': 'Internal server error'}
        )
    