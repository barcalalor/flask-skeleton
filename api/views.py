from flask import jsonify, request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from api.schemas import CamaraSchema
from core.models import Camara
from flask import Blueprint

camaras = Blueprint('camaras', __name__, url_prefix="/camaras")


@camaras.route("/", methods=["GET"])
def list_camaras():
    camaras = Camara.all()
    schema = CamaraSchema()
    response = schema.dump(camaras, many=True)
    return jsonify(response)


@camaras.route("/<int:pk>", methods=["GET"])
def get_camara(pk):
    try:
        camara = Camara.query.get(pk)
    except IntegrityError:
        return {"message": "Camara could not be found."}, 400
    schema = CamaraSchema()
    response = schema.dump(camara, many=True)
    return jsonify(response)


@camaras.route("/", methods=["POST"])
def create_camaras():
    json_data = request.get_json()
    schema = CamaraSchema()
    try:
        data = schema.load(json_data)
        camara = Camara.get_by(url=data['url'])
        if not camara:
            new_camara = Camara().create(**data)
            if new_camara:
                new_camara.save()
                response = schema.dump(new_camara)
                return jsonify(response)
        else:
            return jsonify("DUPE")
    except ValidationError as err:
        return jsonify(err.messages, 400)
