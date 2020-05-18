from app import db


class Status(db.Model):
    __tablename__ = 'Status'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'description': self.description
        }
