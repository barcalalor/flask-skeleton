from core.mixins import PkModel
from database import db


class Camara(PkModel):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    lens = db.Column(db.Integer)
    azimuth = db.Column(db.Float)
    elevation = db.Column(db.Float)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    ground_elevation = db.Column(db.Integer)
    start_record_datetime = db.Column(db.DateTime, nullable=True)
    stop_record_datetime = db.Column(db.DateTime, nullable=True)
