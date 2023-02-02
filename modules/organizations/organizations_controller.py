

from config.database import SessionLocal

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

    
    def create_organization( self, organization ):
        new_organization = Organization_model( **organization.dict() )
        self.db.add( new_organization  )
        self.db.commit()
        self.db.refresh( new_organization )
        return new_organization


    def update_organization( self, id: int, organization ):
        organization_DB = self.get_organization( id )
        if not organization_DB:
            return []
        organization_DB.update( **organization.__dict__ )
        self.db.commit()
        self.db.refresh( organization_DB )
        return True


    def delete_organization( self, organization ):
        self.db.delete( organization )
        self.db.commit()
        return
