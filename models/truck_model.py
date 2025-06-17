from datetime import datetime, timezone

from db import db

class TruckModel(db.Model):
    __tablename__ = 'truck'

    id = db.Column(db.Integer, primary_key=True)
    renavam = db.Column(db.String(11), unique=True, nullable=False)
    plate = db.Column(db.String(20), unique=True, nullable=False)
    model = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100), nullable=True)
    
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)