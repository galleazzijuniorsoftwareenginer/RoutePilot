from pydantic import BaseModel


class VehicleCreate(BaseModel):
    plate: str
    capacity: int
    company_id: int


class VehicleResponse(BaseModel):
    id: int
    plate: str
    capacity: int
    company_id: int

    class Config:
        from_attributes = True
