from os import abort
from flask import Blueprint, jsonify, request, make_response
from app.models.pin import Pin
from app import db

pin_bp = Blueprint("pin_bp", __name__, url_prefix="/pin")

@pin_bp.route('', methods=['POST'])
def create_one_pin():
    request_body = request.get_json()
    if "latitude" and "longitude" and "description" not in request_body:
        return jsonify({
            "details": "Invalid data"
        }), 400
    new_pin = Pin(latitude=request_body["latitude"], longitude=request_body["longitude"], description=request_body["description"])
    db.session.add(new_pin)
    db.session.commit()
    return jsonify({
        "details": "Pin successfully created"
    }), 201

@pin_bp.route('', methods=['GET'])
def get_all_pins():
    pins_response = []
    all_pins = Pin.query.all()

    for pin in all_pins:
        pins_response.append(pin.to_dict())
    return jsonify(pins_response)
    
@pin_bp.route('<id>', methods=['GET'])
def get_one_pin(id):
    chosen_pin = get_pin_from_id(id)
    return jsonify ({
        "pin": chosen_pin.to_dict()
    }), 200

@pin_bp.route('/<id>', methods=['DELETE'])
def delete_one_pin(id):
    pin = get_pin_from_id(id)
    db.session.delete(pin)
    db.session.commit()
    return jsonify({
        "details": "Pin successfully deleted"
        }), 200

@pin_bp.route('', methods=['DELETE'])
def delete_all_pins():
    Pin.query.delete()
    db.session.commit()
    return jsonify({
        "details": "All pins successfully deleted"
    }), 200

def get_pin_from_id(id):
    try:
        id = int(id)
    except ValueError:
        return abort(make_response({"msg":f"Invalid data type: {id}"}, 400))
    chosen_pin = Pin.query.get(id)

    if chosen_pin is None:
        return abort(make_response({"msg": f"Could not find pin item with id: {id}"}, 404))
    return chosen_pin

