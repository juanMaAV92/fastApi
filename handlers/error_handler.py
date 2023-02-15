

from fastapi import FastAPI, Request, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class ErrorHandler( BaseHTTPMiddleware ):
    def __init__( self, app: FastAPI ) -> None:
        super().__init__( app )

    async def dispatch( self, request: Request, call_next ) -> Response or JSONResponse:
        try:
            return await call_next( request )
        except Exception as e:
            return JSONResponse( status_code= 500, content={ 'error': str(e) } )
        


async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content= { 'error' : str(exc.detail)} )



async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code= 400,
        content=jsonable_encoder({"detail": exc.errors(), "Error": "Name field is missing"}),
    )
