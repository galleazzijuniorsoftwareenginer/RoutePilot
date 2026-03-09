from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order import Order
from app.models.route import Route
from app.models.visit import Visit

import polyline
from app.services.route_stats_service import get_route_stats

from app.services.optimization_service import optimize_route
from app.services.route_stats_service import get_route_stats
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/routes", tags=["Routes"])


@router.post("/generate")
def generate_route(company_id: int, driver_id: int, vehicle_id: int, db: Session = Depends(get_db)):

    orders = db.query(Order).filter(Order.company_id == company_id).all()

    if not orders:
        return {"message": "No orders found"}

    locations = [(o.latitude, o.longitude) for o in orders]

    optimized = optimize_route(locations)

    route = Route(
        company_id=company_id,
        driver_id=driver_id,
        vehicle_id=vehicle_id
    )

    db.add(route)
    db.commit()
    db.refresh(route)

    for sequence, index in enumerate(optimized):

        visit = Visit(
            route_id=route.id,
            order_id=orders[index].id,
            sequence=sequence
        )

        db.add(visit)

    db.commit()

    return {
        "route_id": route.id,
        "optimized_route": [orders[i].id for i in optimized]
    }
from app.models.visit import Visit
from app.models.order import Order


@router.get("/{route_id}")
def get_route(route_id: int, db: Session = Depends(get_db)):

    visits = (
        db.query(Visit)
        .filter(Visit.route_id == route_id)
        .order_by(Visit.sequence)
        .all()
    )

    if not visits:
        return {"message": "Route not found"}

    deliveries = []

    coordinates = []

    for visit in visits:

        order = db.query(Order).filter(Order.id == visit.order_id).first()

        deliveries.append({
            "order_id": order.id,
            "customer": order.customer_name,
            "address": order.address,
            "sequence": visit.sequence,
            "latitude": order.latitude,
            "longitude": order.longitude
        })

        coordinates.append(f"{order.latitude},{order.longitude}")

    # gerar link Google Maps

    maps_url = "https://www.google.com/maps/dir/" + "/".join(coordinates)

    return {
        "route_id": route_id,
        "stops": deliveries,
        "google_maps_url": maps_url
    }
@router.get("/{route_id}/stats")
def route_stats(route_id: int, db: Session = Depends(get_db)):

    visits = (
        db.query(Visit)
        .filter(Visit.route_id == route_id)
        .order_by(Visit.sequence)
        .all()
    )

    if not visits:
        return {"message": "Route not found"}

    coordinates = []

    for visit in visits:

        order = db.query(Order).filter(Order.id == visit.order_id).first()

        coordinates.append([
            order.longitude,
            order.latitude
        ])

    stats = get_route_stats(coordinates)

    return {
        "route_id": route_id,
        "coordinates": coordinates,
        "distance_km": stats["distance_km"],
        "duration_minutes": stats["duration_minutes"],
        "polyline": stats["polyline"]
    }

@router.get("/{route_id}/map", response_class=HTMLResponse)
def show_route_map(route_id: int, db: Session = Depends(get_db)):

    visits = (
        db.query(Visit)
        .filter(Visit.route_id == route_id)
        .order_by(Visit.sequence)
        .all()
    )

    if not visits:
        return "<h1>Route not found</h1>"

    coordinates = []

    markers = []

    for visit in visits:

        order = db.query(Order).filter(Order.id == visit.order_id).first()

        coordinates.append([order.longitude, order.latitude])

        markers.append({
            "lat": order.latitude,
            "lng": order.longitude,
            "name": order.customer_name
        })

    stats = get_route_stats(coordinates)

    decoded = polyline.decode(stats["polyline"])

    polyline_js = ",".join([f"[{lat},{lng}]" for lat, lng in decoded])

    markers_js = ""

    for i, m in enumerate(markers):

        markers_js += f"""
        L.marker([{m['lat']}, {m['lng']}])
        .addTo(map)
        .bindPopup("{i+1} - {m['name']}");
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>

    <title>RoutePilot Map</title>

    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

    </head>

    <body>

    <h2>Route {route_id}</h2>

    <div id="map" style="height:600px;"></div>

    <script>

    var map = L.map('map').setView([{markers[0]['lat']},{markers[0]['lng']}], 13);

    L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
        maxZoom: 19
    }}).addTo(map);

    {markers_js}

    var routeLine = L.polyline([{polyline_js}], {{color:'red', weight:5}}).addTo(map);

    map.fitBounds(routeLine.getBounds());

    </script>

    </body>
    </html>
    """

    return html
