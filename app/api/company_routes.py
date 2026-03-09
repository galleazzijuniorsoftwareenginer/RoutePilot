from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.company import Company
from app.schemas.company_schema import CompanyCreate, CompanyResponse


router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("/", response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):

    new_company = Company(
        name=company.name,
        email=company.email
    )

    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company


@router.get("/", response_model=list[CompanyResponse])
def get_companies(db: Session = Depends(get_db)):

    companies = db.query(Company).all()
    return companies


@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db)):

    company = db.query(Company).filter(Company.id == company_id).first()

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    return company


@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):

    company = db.query(Company).filter(Company.id == company_id).first()

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    db.delete(company)
    db.commit()

    return {"message": "Company deleted"}
