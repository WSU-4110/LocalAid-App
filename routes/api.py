from flask import Blueprint, request, jsonify
from models import HelpRequest, db

api_routes = Blueprint('api', __name__)

@api_routes.route('/request_help', methods=['POST'])
def request_help():
    data = request.json
    new_request = HelpRequest(
        name=data['name'],
        description=data['description'],
        location=data['location'],
        contact=data['contact']
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'message': 'Help request submitted successfully'}), 201

@api_routes.route('/get_requests', methods=['GET'])
def get_requests():
    requests = HelpRequest.query.all()
    return jsonify([{
        'id': r.id,
        'name': r.name,
        'description': r.description,
        'location': r.location,
        'contact': r.contact
    } for r in requests])
