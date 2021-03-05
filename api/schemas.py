from marshmallow import Schema, fields


class CamaraSchema(Schema):
    id = fields.Integer()
    url = fields.String()
    lens = fields.Integer()
    azimuth = fields.Float()
    elevation = fields.Float()
    width = fields.Integer()
    height = fields.Integer()
    ground_elevation = fields.Integer()
    start_record_datetime = fields.DateTime(required=False)
    stop_record_datetime = fields.DateTime(required=False)
