


from sqlalchemy import TIMESTAMP, Column, Integer, String, text

from config.database import Base

class Organization( Base ):
    __tablename__ = 'organizations'
    id = Column( Integer, primary_key= True, autoincrement= True )
    name = Column( String, nullable= False)
    description = Column( String, nullable= False)
    type = Column( String, nullable= False)
    identification_type = Column( String, nullable= False)
    identification = Column( String, nullable= False)
    address = Column( String, nullable= False)
    phone = Column( String, nullable= False)
    email = Column( String, unique= True,  nullable= False)

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))


    def update( self, **kwargs ):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)