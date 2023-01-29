

from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from modules.company import company_schemas as company_schemas
from modules.company.company_controller import Company_Controller


companyRouter = APIRouter()


@companyRouter.get( '/', tags= [ 'company' ],
                    response_model= company_schemas.List_companies_response )
def get_companies( limit: int = 10, page: int = 1, search: str = '' ) :    
    companies = Company_Controller().get_companies( limit, page, search )
    return JSONResponse(    status_code= 200, 
                            content= { 
                                'results': len( companies ), 
                                'companies': jsonable_encoder( companies) } )



@companyRouter.get( '/{id}', tags= [ 'company' ],
                    response_model= company_schemas.Company_Base_Schema )
def get_company( id: int = Path( ge=1 ) ) :
    company = Company_Controller().get_company( id )
    print( company)
    if not company:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    return JSONResponse(  status_code= 200,
                           content= jsonable_encoder( company ) )



@companyRouter.post( '/', tags= [ 'company' ],
                    response_model= company_schemas.Companies_response )
def create_company( company: company_schemas.Create_Company_Schema ) :
    new_company = Company_Controller().create_company( company )
    return JSONResponse( status_code= 201, content= jsonable_encoder( new_company ))



@companyRouter.put( '/', tags= [ 'company' ],
                    response_model= dict)
def update_company(id: int, company: dict ) :
    company_DB = Company_Controller().update_company( id, company )
    if not company_DB:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    return JSONResponse( status_code= 200, content={ 'message' : 'Actualizado exitosamente' })



@companyRouter.delete( '/{id}', tags= [ 'company' ],
                    response_model= dict )
def delete_companies( id: int = Path( ge=1 ) ) :
    company = Company_Controller().get_company( id )
    if not company:
        return JSONResponse( status_code= 404, content={ 'message' : 'No encontrado' })
    Company_Controller().delete_company( company )
    return JSONResponse( status_code= 200, content={ 'message' : 'Borrado exitosamente' })