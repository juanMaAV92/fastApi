 
__author__ = 'juanMaAV92'

import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from handlers.error_handler import ErrorHandler, http_exception_handler, validation_exception_handler
from modules import organizations
from modules import headquarters
from config.database import engine, Base
from config.config import settings

Base.metadata.create_all( bind= engine )

app= FastAPI(
    title= settings.API_TITLE,
    description= settings.API_DESC,
    version= settings.API_VERSION,
    docs_url= settings.DOCS_URL,
    redoc_url= settings.REDOC_URL
)

app.add_middleware( ErrorHandler )
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.get( f'{settings.URL_PREFIX}health', tags=[ 'health' ] )
async def health():
    # raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return  JSONResponse( status_code= 200, content=[] )


app.include_router( headquarters.headquartersRouter, prefix= f'{settings.URL_PREFIX}organizations/headquarters' )
app.include_router( organizations.organizationRouter, prefix= f'{settings.URL_PREFIX}organizations' )


def run():
    uvicorn.run(    'main:app',
                    host = settings.API_HOST,
                    port = settings.API_PORT,
                    reload = settings.API_RELOAD,
                    log_level = 'debug')


if __name__ == '__main__':
    run()