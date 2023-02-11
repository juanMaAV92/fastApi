

from sqlalchemy import TIMESTAMP, Column, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import relationship

from config.database import Base


class Headquarter( Base ):
    __tablename__ = 'headquarters'
    id = Column( Integer, autoincrement= True )
    name = Column( String, nullable= False)
    address = Column( String, nullable= False)
    phone = Column( String, nullable= False)
    email = Column( String, nullable= False)
    
    organization_id = Column( Integer, nullable=True) 

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))

    organization = relationship("Organization", back_populates="headquarter")
   
    __table_args__ = ( 
        PrimaryKeyConstraint( 'id' ),
        ForeignKeyConstraint( [ 'organization_id' ],[ 'organizations.id' ], ondelete='CASCADE'),
        UniqueConstraint( 'name'),
        UniqueConstraint( 'phone'),
        UniqueConstraint( 'email'),
    )

    def update( self, **kwargs ):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)