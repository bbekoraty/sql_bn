from pydantic import BaseModel
from typing import Optional,List, Dict, Any

class JobBase(BaseModel):
    project: str
    hotspot_type: str
    max_temp: float
    string_tag: str
    priority: int
    
class JobCreate(JobBase):
    pass
    
class Job(JobBase):
    id: int

    class Config:
        orm_mode = True

class putAssign(JobBase):
    
    uid : str
    header : str =""
    worker : str =""
    status : str =""
    
class putAssignGet(putAssign):
    id: int
    
    class Config:
        orm_mode = True
    


