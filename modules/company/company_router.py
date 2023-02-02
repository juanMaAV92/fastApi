

from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from modules.company.company_schemas import *
from modules.company.company_controller import Company_Controller


companyRouter = APIRouter()


@companyRouter.get( '/', tags= [ 'company' ],
                    response_model= Get_organizations_response )
def get_organizations( limit: int = 10, page: int = 1, search: str = '' ) -> Get_organizations_response :    
    organizations = Company_Controller().get_organizations( limit, page, search )
    return JSONResponse(    status_code= 200, 
                            content= { 
                                'results': len( organizations ), 
                                'organizations': jsonable_encoder( organizations) } )



@companyRouter.get( '/{id}', tags= [ 'company' ],
                    response_model= Get_Company_response )
def get_company( id: int = Path( ge=1 ) ) -> Get_Company_response :
    company = Company_Controller().get_company( id )
    if not company:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    return JSONResponse(  status_code= 200,
                           content= jsonable_encoder( company ) )



@companyRouter.post( '/', tags= [ 'company' ],
                    response_model= Create_organizations_response )
def create_company( company: Create_Company_Schema ) -> Create_organizations_response:
    new_company = Company_Controller().create_company( company )
    return JSONResponse(    status_code= 201, 
                            content= jsonable_encoder( Create_organizations_response.formatter(new_company.__dict__) ))



@companyRouter.put( '/', tags= [ 'company' ],
                    response_model= Update_Company_response )
def update_company(id: int, company: Update_Company_Schema ) -> Update_Company_response:
    company_DB = Company_Controller().update_company( id, company )
    if not company_DB:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    return JSONResponse( status_code= 200, content={ 'message' : 'Actualizado exitosamente' })



@companyRouter.delete( '/{id}', tags= [ 'company' ],
                    response_model= dict )
def delete_organizations( id: int = Path( ge=1 ) ) :
    company = Company_Controller().get_company( id )
    if not company:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    Company_Controller().delete_company( company )
    return JSONResponse( status_code= 200, content={ 'message' : 'Borrado exitosamente' })