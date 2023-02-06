


from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from config.database import Base
from modules.organizations.organizations_model import Organization

class Headquarter( Base ):
    __tablename__ = 'headquarters'
    id = Column( Integer, primary_key= True, autoincrement= True )
    name = Column( String, unique= True, nullable= False)
    address = Column( String, nullable= False)
    phone = Column( String, unique= True, nullable= False)
    email = Column( String, unique= True,  nullable= False)
    
    organization_id = Column( Integer, ForeignKey('organizations.id')) 
    organization = relationship( Organization )

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))


    def update( self, **kwargs ):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)