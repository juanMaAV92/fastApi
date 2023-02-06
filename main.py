 
__author__ = 'juanMaAV92'

import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from middlewares.error_handler import ErrorHandler
from middlewares.error_validation import validation_exception_handler
from modules import organizations
from modules.organizations import headquarters
from config.database import engine, Base
from config.config import settings

Base.metadata.create_all( bind= engine )

app= FastAPI(
    title= 'Api',
    description= 'HomeWork 1',
    version= '0.1.0'
)


app.add_middleware( ErrorHandler )
app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.get( f'{settings.URL_PREFIX}health', tags=[ 'health' ] )
def health():
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