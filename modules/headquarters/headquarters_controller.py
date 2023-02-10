

from config.database import SessionLocal
from modules.headquarters.headquarters_model import Headquarter as Headquarters_model

class headquarter_Controller():

    def __init__( self ) -> None:
        self.db =  SessionLocal()
    
    def __del__( self ) -> None:
        self.db.close()


    def get_headquarters( self, limit: int, page: int ) :
        skip = (page - 1) * limit
        headquarters = self.db.query( Headquarters_model ).group_by( Headquarters_model.id ).limit( limit ).offset( skip ).all()
        return headquarters
    
    def get_headquarter( self, id ):
        headquarter = self.db.query( Headquarters_model ).filter( Headquarters_model.id == id ).first()
        return headquarter

    def create_headquarter( self, headquarter ):
        headquarter_DB = self.db.query( Headquarters_model ).filter( Headquarters_model.email == headquarter.email ).first()
        if headquarter_DB:
            return []
        new_headquarter = Headquarters_model( **headquarter.dict() )
        self.db.add( new_headquarter  )
        self.db.commit()
        self.db.refresh( new_headquarter )
        return new_headquarter
   