from pydantic import BaseModel


class DriverCreate(BaseModel):
    name: str
    phone: str
    company_id: int


class DriverResponse(BaseModel):
    id: int
    name: str
    phone: str
    company_id: int

    class Config:
        from_attributes = True
