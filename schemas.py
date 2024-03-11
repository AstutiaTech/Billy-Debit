from pydantic import BaseModel, EmailStr
from  datetime import datetime
from typing import Any, Dict, List, Optional

class BillerCategoryModel(BaseModel):
    id: Optional[int] = 0
    name: Optional[str] = None
    description: Optional[str] = None
    category_code: Optional[str] = None
    
    class Config:
        orm_mode = True

class BillerServiceModel(BaseModel):
    id: Optional[int] = 0
    name: Optional[str] = None
    description: Optional[str] = None
    label_name: Optional[str] = None
    service_code: Optional[str] = None
    amount: Optional[float] = 0
    fee: Optional[float] = 0
    is_flat: Optional[int] = None
    min_amount: Optional[float] = 0
    max_amount: Optional[float] = 0
    
    class Config:
        orm_mode = True

class ValidateBillerModel(BaseModel):
    service_code: str
    customer: str
    
    class Config:
        orm_mode = True

class PayBillModel(BaseModel):
    service_code: str
    customer_id: int
    branch_id: int
    channel_id: int
    nuban: str
    amount: float
    customer: str
    ip_address: str
    
    class Config:
        orm_mode = True

class ResponseModel(BaseModel):
    status: bool
    message: str
    response_code: str
    
    class Config:
        orm_mode = True
        
class ResponseDataMoreModel(BaseModel):
    status: bool
    message: str
    data: Dict[str, Any] = None
    
    class Config:
        orm_mode = True