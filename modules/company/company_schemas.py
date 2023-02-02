
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Company_Base_Schema( BaseModel ):
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
        
    
class Create_Company_Schema( Company_Base_Schema ):
   pass


class Update_Company_Schema( BaseModel ):
   description: Optional[ str ] = Field( max_length=50 )
   address: Optional[ str ]
   phone: Optional[ str ]
   email: Optional[ str ]
   class Config:
        orm_mode = True  


class Get_Company_response( Company_Base_Schema ):
    id: int = None    
    created_at: datetime
    updated_at: datetime

class Get_organizations_response( BaseModel ):
    result: int
    organizations: List[ Get_Company_response ]


class Create_organizations_response( BaseModel ):
    id: int = None
    created_at: datetime
    def formatter( company ):
        return{
            'id': company[ 'id' ],
            'created_at': company[ 'created_at' ]
        }


class Update_Company_response( BaseModel ):
    id: int = None
    updated_at: datetime
    def formatter( company ):
        return{
            'id': company[ 'id' ],
            'updated_at': company[ 'updated_at' ]
        }
