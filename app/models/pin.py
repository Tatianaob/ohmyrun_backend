from app import db

class Pin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    description = db.Column(db.String)


    def to_dict(self):
        pin_dict = {
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "description": self.description
        }
        return pin_dict