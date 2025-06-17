from marshmallow import Schema, fields, validate

class TruckSchema(Schema):
    id = fields.Int(dump_only=True)
    renavam = fields.Str(required=True, validate=validate.Regexp(r'^\d{11}$'))
    plate = fields.Str(required=True, validate=validate.Regexp(r'^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$'))
    model = fields.Str(required=True)
    year = fields.Int(required=True, validate=validate.Range(min=1950, max=2100))
    description = fields.Str()

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)