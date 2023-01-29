

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from config.database import get_db
from modules.company import company_schemas as company_schemas
from modules.company.company_model import Company  as Company_model

companyRouter = APIRouter()


@companyRouter.get( '/', tags= [ 'company' ],
                    response_model= company_schemas.List_companies_response )
def get_companies( db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = '' ) :
    
    skip = (page - 1) * limit
    companies = db.query( Company_model ).group_by( Company_model.id ).filter(
        Company_model.name.contains( search )).limit( limit ).offset( skip ).all()
    return JSONResponse( status_code= 200, content= {'status': 'success', 'results': len( companies ), 'companies': jsonable_encoder( companies )} )



@companyRouter.get( '/company/{id}', tags= [ 'company' ],
                    response_model= company_schemas.Company_Base_Schema )
def get_company() :

    return JSONResponse( status_code= 200)



@companyRouter.post( '/', tags= [ 'company' ],
                    response_model= company_schemas.Companies_response )
def create_company( company: company_schemas.Create_Company_Schema, db: Session = Depends( get_db )) :
    new_company = Company_model( **company.dict() )
    db.add( new_company  )
    db.commit()
    db.refresh( new_company )
    print( 'ddde')
    return JSONResponse( status_code= 201, content= jsonable_encoder( new_company ))



@companyRouter.put( '/company', tags= [ 'company' ],
                    response_model= dict)
def update_company() :

    return JSONResponse( status_code= 200)



@companyRouter.delete( '/company', tags= [ 'company' ],
                    response_model= dict )
def delete_companies() :

    return JSONResponse( status_code= 200)