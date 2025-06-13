from marshmallow import Schema, fields, validate

class DriverSchema(Schema):
    id = fields.UUID(dump_only=True)
    cpf = fields.Str(required=True, validate=validate.Regexp(r'^\d{11}$'))
    cnh = fields.Str(required=True, validate=validate.Length(equal=11))
    categoria_cnh = fields.Str(required=True, validate=validate.OneOf(['A', 'B', 'C', 'D', 'E', 'AB', 'AC', 'AD', 'AE']))
    name = fields.Str(required=True)
    birthday = fields.Date(required=True, format='%Y-%m-%d')
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
