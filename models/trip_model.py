import uuid
from datetime import datetime, timezone

from db import db

class TripModel(db.Model):
    __tablename__ = 'trip'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    end_date = db.Column(db.DateTime(timezone=True), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)

    truck_id = db.Column(db.Integer, db.ForeignKey('truck.id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    truck = db.relationship("TruckModel", back_populates="trips")
    driver = db.relationship("DriverModel", back_populates="trips")

    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc),nullable=False)