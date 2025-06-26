from marshmallow import Schema, fields

class ExternalDataSchema(Schema):
    id = fields.Int(dump_only=True)
    origin = fields.Str(dump_only=True)
    content = fields.Dict(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)