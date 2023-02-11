

from sqlalchemy.sql import text
from config.database import SessionLocal

from modules.headquarters.headquarters_model import Headquarter as Headquarters_model
from modules.organizations.organizations_model import Organization as Organization_model

class organization_Controller():

    def __init__( self ) -> None:
        self.db =  SessionLocal()
    
    def __del__( self ) -> None:
        self.db.close()


    def get_organizations( self, limit: int, page: int, search: str ) :
        skip = (page - 1) * limit
        organizations = self.db.query( Organization_model ).group_by( Organization_model.id ).filter(
        Organization_model.name.contains( search )).limit( limit ).offset( skip ).all()
        return organizations


    def get_organization( self, id ):
        organization = self.db.query( Organization_model ).filter( Organization_model.id == id ).first()
        return organization


    def get_headquarters_by_organization( self, organization_id, limit: int, page: int  ):
        skip = (page - 1) * limit
        headquarters = self.db.query( Headquarters_model ).filter( Headquarters_model.organization_id == organization_id ).limit( limit ).offset( skip ).all()
        return headquarters
    

    
    def create_organization( self, organization ):
        organization_DB = self.db.query( Organization_model ).filter( Organization_model.email == organization.email ).first()
        if organization_DB:
            return []
        new_organization = Organization_model( **organization.dict() )
        self.db.add( new_organization  )
        self.db.commit()
        self.db.refresh( new_organization )
        return new_organization


    def update_organization( self, id: int, organization ):
        organization_DB = self.get_organization( id )
        if not organization_DB:
            return []
        organization_DB.update( **organization.dict(exclude_none=True) )
        self.db.commit()
        self.db.refresh( organization_DB )
        return True


    def delete_organization( self, organization ):
        self.db.delete( organization )
        self.db.commit()
        return
