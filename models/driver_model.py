from datetime import datetime, timezone

from db import db

class DriverModel(db.Model):
    __tablename__ = 'driver'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String, unique=True, nullable=False)
    cnh = db.Column(db.String, unique=True, nullable=False)
    categoria_cnh = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)

    trips = db.relationship("TripModel", back_populates=__tablename__, cascade="all, delete-orphan")
    