
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Company_Base_Schema( BaseModel ):
    # id: Optional[ int ] = None
    name: str = Field( min_length=3, max_length=20 )
    identification_type: str 
    identification: str
    description: Optional[ str ] = Field( max_length=50 )
    address: str
    number: str
    email: str
    class Config:
        orm_mode = True
        schema_extra = {
            'exampe':{
                'id': 1234,
                'name': 'minim sit',
                'description': 'lorem laborum cupidatat consequat cillum ',
                'identification_type': 'nit',
                'identification': '123123213-1',
                'address': 'consectetur eu voluptate amet',
                'number': '1382132323',
                'email': 'juan@hotm.com'
            }
        }
     
    
    
class Create_Company_Schema( Company_Base_Schema ):
   pass

    


class Companies_response( Company_Base_Schema ):
    id: Optional[ int ] = None
    name: str 
    created_at: datetime
    updated_at: datetime

class List_companies_response( BaseModel ):
    status: str
    result: int
    companies: List[ Companies_response ]