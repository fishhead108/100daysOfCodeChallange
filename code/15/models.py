from app import db


class Todos(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return f'<Task №{self.id} - {self.task}>'

    def __str__(self):
        return f'<{self.id} - {self.task}>'
