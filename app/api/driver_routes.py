from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.driver import Driver
from app.schemas.driver_schema import DriverCreate, DriverResponse


router = APIRouter(prefix="/drivers", tags=["Drivers"])


@router.post("/", response_model=DriverResponse)
def create_driver(driver: DriverCreate, db: Session = Depends(get_db)):

    new_driver = Driver(
        name=driver.name,
        phone=driver.phone,
        company_id=driver.company_id
    )

    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)

    return new_driver


@router.get("/", response_model=list[DriverResponse])
def get_drivers(db: Session = Depends(get_db)):

    drivers = db.query(Driver).all()
    return drivers


@router.get("/{driver_id}", response_model=DriverResponse)
def get_driver(driver_id: int, db: Session = Depends(get_db)):

    driver = db.query(Driver).filter(Driver.id == driver_id).first()

    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    return driver


@router.delete("/{driver_id}")
def delete_driver(driver_id: int, db: Session = Depends(get_db)):

    driver = db.query(Driver).filter(Driver.id == driver_id).first()

    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    db.delete(driver)
    db.commit()

    return {"message": "Driver deleted"}
