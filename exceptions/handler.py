from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from config import Config, Environment

async def exception_handler(_: Request, exc: Exception):
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={'detail': exc.detail,}
        )
    elif isinstance(exc, ValidationError):
        try:
            detail = [{'field': err['loc'][0], 'message': err['msg']} for err in exc.errors()]
            return JSONResponse(
                status_code=400,
                content={'detail': 'Invalid input', 'fields': detail}
            )
        except Exception:
            pass
    
    if Config.environment == Environment.PRODUCTION:
        return JSONResponse(
            status_code=500,
            content={'detail': 'Internal server error'}
        )
    else:
        print(exc)
        return JSONResponse(
            status_code=500,
            content={'detail': str(exc)}
        )
    