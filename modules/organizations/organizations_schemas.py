
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Organization_Base_Schema( BaseModel ):
    # id: Optional[ int ] = None
    name: str = Field( min_length=3, max_length=20 )
    type: str 
    identification_type: str 
    identification: str
    description: Optional[ str ] = Field( max_length=50 )
    address: str
    phone: str
    email: str
    class Config:
        orm_mode = True     
        

class Get_organization_response( Organization_Base_Schema ):
    id: int = None    
    created_at: datetime
    updated_at: datetime


class Get_organizations_response( List[ Get_organization_response ] ):
    pass


class Create_organization_Schema( Organization_Base_Schema ):
   pass


class Create_organizations_response( BaseModel ):
    id: int = None
    created_at: datetime
    def formatter( company ):
        return{
            'id': company[ 'id' ],
            'created_at': company[ 'created_at' ]
        }

class Update_organization_Schema( BaseModel ):
   description: Optional[ str ] = Field( max_length=50 )
   address: Optional[ str ]
   phone: Optional[ str ]
   email: Optional[ str ]
   class Config:
        orm_mode = True  


class Update_organization_response( BaseModel ):
    id: int = None
    updated_at: datetime
    def formatter( organization ):
        return{
            'id': organization[ 'id' ],
            'updated_at': organization[ 'updated_at' ]
        }
