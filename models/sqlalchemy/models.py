from app import db

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    species = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    breed = db.Column(db.String(255))  # New field for breed
    photo_url = db.Column(db.String(255))  # New field for photo URL
    # ... any other existing fields ...

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'age': self.age,
            'breed': self.breed,  # Include breed in the dictionary
            'photo_url': self.photo_url,  # Include photo URL in the dictionary
        }