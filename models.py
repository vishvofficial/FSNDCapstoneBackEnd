from app import db


class Student(db.Model):

    __tablename__ = 'Student'

    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer, unique=True, nullable=False)
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
            'sid': self.sid,
            'mobile': self.mobile,
            'email': self.email
        }

    def get_tasks(self):
        result = Task.query.filter(
            Task.sid == self.sid
        )
        return [task.serialize for task in result]


class Teacher(db.Model):

    __tablename__ = 'Teacher'

    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer, unique=True, nullable=False)
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


class Status(db.Model):

    __tablename__ = 'Status'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
