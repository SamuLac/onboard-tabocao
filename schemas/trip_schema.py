from marshmallow import Schema, fields
from schemas import DriverSchema, TruckSchema

class TripSchema(Schema):
    id = fields.Int(dump_only=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    origin = fields.Str(required=True)
    destination = fields.Str(required=True)

    truck_id = fields.Int(required=True, load_only=True)
    driver_id = fields.Int(required=True, load_only=True)

    truck = fields.Nested(TruckSchema, dump_only=True)
    driver = fields.Nested(DriverSchema, dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)