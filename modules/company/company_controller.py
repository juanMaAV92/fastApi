

from config.database import SessionLocal

from modules.company.company_model import Company  as Company_model

class Company_Controller():

    def __init__( self ) -> None:
        self.db =  SessionLocal()
    
    def __del__( self ) -> None:
        self.db.close()


    def get_companies( self, limit: int, page: int, search: str ) :
        skip = (page - 1) * limit
        companies = self.db.query( Company_model ).group_by( Company_model.id ).filter(
        Company_model.name.contains( search )).limit( limit ).offset( skip ).all()
        return companies


    def get_company( self, id ):
        company = self.db.query( Company_model ).filter( Company_model.id == id ).first()
        return company

    
    def create_company( self, company ):
        new_company = Company_model( **company.dict() )
        self.db.add( new_company  )
        self.db.commit()
        self.db.refresh( new_company )
        return new_company


    def update_company( self, id: int, company ):
        company_DB = self.get_company( id )
        if not company_DB:
            return []
        company_DB.update( **company.__dict__ )
        self.db.commit()
        self.db.refresh( company_DB )
        return True


    def delete_company( self, company ):
        self.db.delete( company )
        self.db.commit()
        return
