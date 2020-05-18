from app import db
from .task import Task


class Teacher(db.Model):
    __tablename__ = 'Teacher'

    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.BigInteger, unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'tid': self.tid,
            'mobile': self.mobile,
            'email': self.email
        }

    def get_tasks(self):
        result = Task.query.filter(
            Task.tid == self.tid
        )
        return [task.serialize for task in result]
