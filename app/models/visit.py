from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base


class Visit(Base):

    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True)

    route_id = Column(Integer, ForeignKey("routes.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))

    sequence = Column(Integer)
