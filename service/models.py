from service import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(256), nullable=True)
    phone_number = db.Column(db.String(32), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone_number": self.phone_number
        }
    
    def deserialize(self, data):
        if "name" in data:
            self.name = data.get("name")
        if "email" in data:
            self.email = data.get("email")
        if "address" in data:
            self.address = data.get("address")
        if "phone_number" in data:
            self.phone_number = data.get("phone_number")
        return self
