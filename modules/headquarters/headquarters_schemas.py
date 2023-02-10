
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Headquarter_Base_Schema( BaseModel ):
    # id: Optional[ int ] = None
    name: str = Field( min_length=3, max_length=20 )    
    address: str
    phone: str
    email: str
    organization_id: Optional[ int ] = None    
    class Config:
        orm_mode = True     


class Get_headquarter_response( Headquarter_Base_Schema ):
    id: int = None    
    created_at: datetime
    updated_at: datetime


class Get_headquarters_response( List[Get_headquarter_response] ):
    pass


class Create_headquarter_Schema( Headquarter_Base_Schema ):
   pass


class Create_headquarter_response( BaseModel ):
    id: int = None
    created_at: datetime
    def formatter( company ):
        return{
            'id': company[ 'id' ],
            'created_at': company[ 'created_at' ]
        }