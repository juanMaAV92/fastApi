

from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from modules.headquarters.headquarters_schemas import *
from modules.headquarters.headquarters_controller import headquarter_Controller


headquartersRouter = APIRouter()



@headquartersRouter.get( '', tags= [ 'headquarters' ],
                    response_model= Get_headquarters_response )
async def get_headquarters( limit: int = 10, page: int = 1, search: str = '' ) -> Get_headquarters_response :   
    print('ho') 
    headquarters = headquarter_Controller().get_headquarters( limit, page )
    return JSONResponse(    status_code= 200, 
                            content= jsonable_encoder( headquarters ) )


@headquartersRouter.get( '/{id}', tags= [ 'headquarters' ],
                    response_model= Get_headquarter_response )
async def get_headquarter( id: int = Path( ge=1 ) ) -> Get_headquarter_response :
    headquarter = headquarter_Controller().get_headquarter( id )
    if not headquarter:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    return JSONResponse(  status_code= 200,
                           content= jsonable_encoder( headquarter ) )


@headquartersRouter.post( '', tags= [ 'headquarters' ],
                    response_model= Create_headquarter_response )
async def create_headquarter( headquarter: Create_headquarter_Schema ) -> Create_headquarter_response:
    new_headquarter = headquarter_Controller().create_headquarter( headquarter )
    if not new_headquarter:
        return JSONResponse(    status_code= 400, 
                                content= { 'message' : 'the email must be unique' }
        )
    return JSONResponse(    status_code= 200, 
                            content= jsonable_encoder( Create_headquarter_response.formatter(new_headquarter.__dict__) ))

