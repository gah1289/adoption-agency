from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()


class Pet(db.Model):
    '''Pet Model'''
    __tablename__="pets"

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.Text, nullable=False)
    species=db.Column(db.Text, nullable=False)
    photo_url=db.Column(db.Text, nullable=True)
    age=db.Column(db.Integer, nullable=True)
    notes=db.Column(db.Text, nullable=True)
    available=db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Pet {self.id} name={self.name} species={self.species}>"

def connect_db(app):
    db.app=app
    db.init_app(app)
