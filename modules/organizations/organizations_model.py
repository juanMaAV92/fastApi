

import enum
from sqlalchemy import TIMESTAMP, Column, Enum, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import relationship

from config.database import Base


class  identification_type_enum( enum.Enum ):
    NIT = 1
    CC  = 2
    

class Organization( Base ):
    __tablename__ = 'organizations'
    id = Column( Integer, autoincrement= True )
    name = Column( String, nullable= False)
    description = Column( String, nullable= False)
    type = Column( String, nullable= False)
    # identification_type = Column( Enum( identification_type_enum ))
    identification_type = Column( String, nullable= False)
    identification = Column( String,  nullable= False)
    address = Column( String, nullable= False)
    phone = Column( String, nullable= False)
    email = Column( String, nullable= False)

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    
    headquarter = relationship(    'Headquarter', 
                                    back_populates= "organization",
                                    passive_deletes=False
                                      )

    __table_args__ = ( 
        PrimaryKeyConstraint('id'),
        UniqueConstraint('identification_type', 'identification', name='uniq_1' ),
        UniqueConstraint( 'name'),
        UniqueConstraint( 'phone'),
        UniqueConstraint( 'email'),
    )


    def update( self, **kwargs ):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)