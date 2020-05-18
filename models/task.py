from app import db


class Task(db.Model):
    __tablename__ = 'Task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.TEXT)
    status = db.Column(db.Integer, db.ForeignKey('Status.id'), nullable=False, default=0)
    progress = db.Column(db.Integer, nullable=False, default=0)
    sid = db.Column(db.Integer, db.ForeignKey('Student.sid'), nullable=False)
    student = db.relationship('Student', backref=db.backref('tasks', cascade='all, delete'))
    tid = db.Column(db.Integer, db.ForeignKey('Teacher.tid'), nullable=False)
    teacher = db.relationship('Teacher', backref=db.backref('tasks', cascade='all, delete'))

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
            'name': self.name,
            'description': self.description,
            'progress': self.progress,
            'sid': self.sid,
            'tid': self.tid,
            'status': self.status
        }
