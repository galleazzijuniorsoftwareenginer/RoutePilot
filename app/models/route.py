from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from app.database import Base


class Route(Base):

    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)

    driver_id = Column(Integer, ForeignKey("drivers.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    created_at = Column(DateTime, default=datetime.utcnow)

