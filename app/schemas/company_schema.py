from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    email: str


class CompanyResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
