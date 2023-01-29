

__author__ = 'juanMaAV92'

import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from middlewares.error_handler import ErrorHandler
from modules import company
from config.database import engine, Base

Base.metadata.create_all( bind= engine )

app= FastAPI(
    title= 'Api',
    description= 'HomeWork 1',
    version= '0.0.1'
)

app.add_middleware( ErrorHandler )

load_dotenv()
API_PORT = int( os.getenv( 'API_PORT' ) )
API_HOST = os.getenv( 'API_HOST' )
API_RELOAD = bool( os.getenv( 'API_PORT' ) )


@app.get( '/health', tags=[ 'health' ] )
def health():
    return  JSONResponse( status_code= 200, content=[] )


app.include_router( company.companyRouter, prefix='/api/v1/companies' )


def run():
    uvicorn.run(    'main:app',
                    host = API_HOST,
                    port = API_PORT,
                    reload = API_RELOAD,
                    log_level = 'debug')


if __name__ == '__main__':
    run()