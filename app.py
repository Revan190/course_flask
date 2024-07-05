# app.py

from flask import Flask, jsonify, request
from models.sqlalchemy.models import Animal, db
from photo_fetcher import fetch_dog_photo, fetch_cat_photo
from settings import settings
from database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.sqlalchemy_database_uri

db = init_db(app)

# Health Check Endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

# Create Animal Endpoint
@app.route('/animal', methods=['POST'])
def create_animal():
    animal_data = request.get_json()
    photo_url = None

    if animal_data['type'].lower() == 'dog':
        photo_url = fetch_dog_photo()
    elif animal_data['type'].lower() == 'cat':
        photo_url = fetch_cat_photo()

    if photo_url:
        new_animal = Animal(
            name=animal_data['name'],
            type=animal_data['type'],
            breed=animal_data.get('breed', 'Unknown'),  # Optional field with default value
            photo_url=photo_url
        )
        db.session.add(new_animal)
        db.session.commit()
        return jsonify(new_animal.to_dict()), 201
    else:
        return jsonify({"error": "Could not fetch photo"}), 500

# Update Animal Endpoint
@app.route('/animal/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    # Your logic to update an animal record with the new fields
    pass

# ... other routes ...

if __name__ == '__main__':
    app.run(debug=True)