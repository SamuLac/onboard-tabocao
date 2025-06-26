from datetime import datetime, timezone

from db import db


class ExternalDataModel(db.Model):
    __tablename__ = 'external_data'

    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    content = db.Column(db.JSON, nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)