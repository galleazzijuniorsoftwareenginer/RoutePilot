from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_name: str
    address: str
    latitude: float
    longitude: float
    company_id: int


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    address: str
    latitude: float
    longitude: float
    status: str
    company_id: int

    class Config:
        from_attributes = True
