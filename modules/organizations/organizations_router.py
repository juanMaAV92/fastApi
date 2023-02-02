

from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from modules.organizations.organizations_schemas import *
from modules.organizations.organizations_controller import organization_Controller


organizationRouter = APIRouter()


@organizationRouter.get( '/', tags= [ 'organization' ],
                    response_model= Get_organizations_response )
def get_organizations( limit: int = 10, page: int = 1, search: str = '' ) -> Get_organizations_response :    
    organizations = organization_Controller().get_organizations( limit, page, search )
    return JSONResponse(    status_code= 200, 
                            content= { 
                                'results': len( organizations ), 
                                'organizations': jsonable_encoder( organizations) } )



@organizationRouter.get( '/{id}', tags= [ 'organization' ],
                    response_model= Get_organization_response )
def get_organization( id: int = Path( ge=1 ) ) -> Get_organization_response :
    organization = organization_Controller().get_organization( id )
    if not organization:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    return JSONResponse(  status_code= 200,
                           content= jsonable_encoder( organization ) )



@organizationRouter.post( '/', tags= [ 'organization' ],
                    response_model= Create_organizations_response )
def create_organization( organization: Create_organization_Schema ) -> Create_organizations_response:
    new_organization = organization_Controller().create_organization( organization )
    return JSONResponse(    status_code= 201, 
                            content= jsonable_encoder( Create_organizations_response.formatter(new_organization.__dict__) ))



@organizationRouter.put( '/', tags= [ 'organization' ],
                    response_model= Update_organization_response )
def update_organization(id: int, organization: Update_organization_Schema ) -> Update_organization_response:
    organization_DB = organization_Controller().update_organization( id, organization )
    if not organization_DB:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    return JSONResponse( status_code= 200, content={ 'message' : 'Actualizado exitosamente' })



@organizationRouter.delete( '/{id}', tags= [ 'organization' ],
                    response_model= dict )
def delete_organizations( id: int = Path( ge=1 ) ) :
    organization = organization_Controller().get_organization( id )
    if not organization:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    organization_Controller().delete_organization( organization )
    return JSONResponse( status_code= 200, content={ 'message' : 'Borrado exitosamente' })