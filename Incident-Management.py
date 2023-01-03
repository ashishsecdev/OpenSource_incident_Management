import os.path
import random
import string

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'incidents.db') ##Creating local db using path where script exist.
db = SQLAlchemy(app)

def ref_func():
    return ''.join(random.choices(string.digits, k=4)) #string.ascii_letters

class Incident(db.Model): ##Table Declaration & Schema - You can update more columns as required and define the required attributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=True)
    assignee = db.Column(db.String(50), nullable=True)
    ref = db.Column(db.String(50), nullable=False)

ref="www.Dummy_Incident.com/INC000"+ref_func() # TO get variable value to return the ticket number.

@app.route('/incidents', methods=['POST']) # Check methods.
def create_incident():
    #data = request.get_json() # Rendering data from HTMl doesnt require JSON, try TINKER for GUI that works. Error for {'Content-Type': 'application/json'}.
    data = request.form
    new_incident = Incident(title=data['title'], category=data['category'], description=data['description'], status='Open', ref=ref)
    db.session.add(new_incident)
    db.session.commit()
    return ref.rsplit("/"), 201 # Gives Ticket portal and ticket number for reference
    #return 'Incident created', 201

@app.route('/incidents/<int:incident_id>', methods=['PUT'])
def update_incident(incident_id):
    data = request.get_json()
    incident = Incident.query.get(incident_id)
    incident.title = data['title']
    incident.category = data['category']
    incident.description = data['description']
    incident.status = data['status']
    incident.assignee = data['assignee']
    incident.ref = data['ref']
    db.session.commit()
    return 'Incident updated', 200

@app.route('/incidents/<int:incident_id>', methods=['DELETE'])
def delete_incident(incident_id):
    incident = Incident.query.get(incident_id)
    db.session.delete(incident)
    db.session.commit()
    return 'Incident deleted', 200

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    results = []
    for incident in incidents:
        obj = {
            'id': incident.id,
            'title': incident.title,
            'category': incident.category,
            'description': incident.description,
            'status': incident.status,
            'assignee': incident.assignee,
            'ref': incident.ref
        }
        results.append(obj)
    return jsonify(results)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1',port=8000,debug=True) #Test locally using - http://127.0.0.1:8000/incidents or update accoridngly.
