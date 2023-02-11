

from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modules.headquarters.headquarters_controller import headquarter_Controller

from modules.organizations.organizations_schemas import *
from modules.organizations.organizations_controller import organization_Controller


organizationRouter = APIRouter()



@organizationRouter.get( '', tags= [ 'organization' ],
                    response_model= Get_organizations_response )
async def get_organizations( limit: int = 10, page: int = 1, search: str = '' ) -> Get_organizations_response :    
    organizations = organization_Controller().get_organizations( limit, page, search )
    return JSONResponse(    status_code= 200, 
                            content= jsonable_encoder( organizations) )


@organizationRouter.get( '/{id}', tags= [ 'organization' ],
                    response_model= Get_organization_response )
async def get_organization( id: int = Path( ge=1 ) ) -> Get_organization_response :
    organization = organization_Controller().get_organization( id )
    if not organization:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    return JSONResponse(  status_code= 200,
                           content= jsonable_encoder( organization ) )


@organizationRouter.get( '/{organization_id}/headquarters')
async def get_headquarters_by_organization( organization_id: int = Path( ge=1 ), limit: int = 10, page: int = 1 ):
    headquarters = organization_Controller().get_headquarters_by_organization( organization_id, limit, page )
    return JSONResponse(    status_code= 200, 
                            content= jsonable_encoder( headquarters ) )


@organizationRouter.post( '', tags= [ 'organization' ],
                    response_model= Create_organizations_response )
async def create_organization( organization: Create_organization_Schema ) -> Create_organizations_response:
    new_organization = organization_Controller().create_organization( organization )
    if not new_organization:
        return JSONResponse(    status_code= 400, 
                                content= { 'message' : 'the email must be unique' }
        )
    return JSONResponse(    status_code= 200, 
                            content= jsonable_encoder( Create_organizations_response.formatter(new_organization.__dict__) ))



@organizationRouter.patch( '/{id}', tags= [ 'organization' ],
                    response_model= Update_organization_response )
async def update_organization(id: int, organization: Update_organization_Schema ) -> Update_organization_response:
    organization_DB = organization_Controller().update_organization( id, organization )
    if not organization_DB:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    return JSONResponse( status_code= 200, content={ 'message' : 'Actualizado exitosamente' })



@organizationRouter.delete( '/{id}', tags= [ 'organization' ],
                    response_model= dict )
async def delete_organizations( id: int = Path( ge=1 ) ) :
    organization = organization_Controller().get_organization( id )
    if not organization:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    organization_Controller().delete_organization( organization )
    return JSONResponse( status_code= 200, content={ 'message' : 'Borrado exitosamente' })