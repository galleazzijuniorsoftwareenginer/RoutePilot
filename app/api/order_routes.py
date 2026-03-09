from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order import Order
from app.schemas.order_schema import OrderCreate, OrderResponse


router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):

    new_order = Order(
        customer_name=order.customer_name,
        address=order.address,
        latitude=order.latitude,
        longitude=order.longitude,
        company_id=order.company_id
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


@router.get("/", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):

    orders = db.query(Order).all()
    return orders


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):

    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):

    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(order)
    db.commit()

    return {"message": "Order deleted"}
