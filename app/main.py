from fastapi import FastAPI
from app.database import engine, Base

from app.models import company, driver, vehicle, order, route, visit

from app.api.company_routes import router as company_router

from app.api.driver_routes import router as driver_router
from app.api.order_routes import router as order_router
from app.api.vehicle_routes import router as vehicle_router
Base.metadata.create_all(bind=engine)
from app.api.route_routes import router as route_router

app = FastAPI(
    title="RoutePilot API",
    description="Logistics and route optimization platform",
    version="0.1.0"
)

app.include_router(company_router)
app.include_router(driver_router)
app.include_router(vehicle_router)
app.include_router(order_router)
app.include_router(route_router)

@app.get("/")
def root():
    return {"message": "RoutePilot API is running"}
