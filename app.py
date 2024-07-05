from flask import Flask, jsonify, request
from models.sqlalchemy.models import Animal, db
from photo_fetcher import fetch_dog_photo, fetch_cat_photo

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    # Simple health check endpoint
    return jsonify({'status': 'healthy'}), 200

@app.route('/animal', methods=['GET', 'POST'])
def animal():
    if request.method == 'GET':
        # Fetch all animals from the database
        animals = Animal.query.all()
        return jsonify([animal.to_dict() for animal in animals])
    elif request.method == 'POST':
        # Add a new animal to the database
        data = request.get_json()
        new_animal = Animal(
            name=data['name'],
            species=data['species'],
            age=data['age'],
            breed=data['breed']
        )
        # Fetch photo URL based on the breed
        if new_animal.species.lower() == 'dog':
            new_animal.photo_url = fetch_dog_photo(new_animal.breed)
        elif new_animal.species.lower() == 'cat':
            new_animal.photo_url = fetch_cat_photo(new_animal.breed)
        
        db.session.add(new_animal)
        db.session.commit()
        return jsonify(new_animal.to_dict()), 201

# ... rest of the file ...

if __name__ == '__main__':
    app.run(debug=True)