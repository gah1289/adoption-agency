from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired

species=["Dog", "Cat", "Porcupine"]

class AddPetForm(FlaskForm):
    '''Form for adding pets'''

    name=StringField("Pet Name", validators=[InputRequired(message="Pet Name can't be blank")])
    species=SelectField("Species", choices=[('dog', 'Dog'), ('cat', 'Cat'), ('por', 'Porcupine')])
    photo_url=StringField("Photo URL")
    age=IntegerField("Age")
    notes=StringField("Notes")

class EditPetForm(FlaskForm):
    '''Form for adding pets'''

    name=StringField("Pet Name", validators=[InputRequired(message="Pet Name can't be blank")])
    species=SelectField("Species", choices=[('dog', 'Dog'), ('cat', 'Cat'), ('por', 'Porcupine')])
    photo_url=StringField("Photo URL")
    age=IntegerField("Age")
    notes=StringField("Notes")
    available=BooleanField("Available?")