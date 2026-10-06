from pydantic import BaseModel, ConfigDict, Field
from typing import List

class OrderItemCreate(BaseModel):
    product_id: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)
    unit_price: float = Field(..., gt=0)

class OrderItemResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    subtotal: float
    
    model_config = ConfigDict(from_attributes=True)

class OrderResponse(BaseModel):
    id: str
    customer_id: str
    status: str
    total_amount: float
    items: List[OrderItemResponse]
    
    model_config = ConfigDict(from_attributes=True)