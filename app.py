from flask import Flask, url_for, render_template, redirect, flash, jsonify

# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "hopperdude"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# debug=DebugToolbarExtension(app)

@app.route('/')
def home_page():
    '''Show home page'''
    pets=Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    '''Render add pet form'''
    form=AddPetForm()    
    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        print('*****************') 
        pet=Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()     
        msg=f"{name} the {species} had been added to the list of adoptable pets!" 
        flash(msg)  
        return redirect('/')
    else:    
        return render_template('add_pet.html',form=form)

@app.route('/pet_info/<id>')
def view_pet(id):
    '''View pet info'''
    pet=Pet.query.get_or_404(id)
    return render_template('pet_info.html', pet=pet)

@app.route('/edit/<id>', methods=["GET", "POST"])
def edit_pet(id):
    '''Edit pet'''
    pet=Pet.query.get_or_404(id)
    form=EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name=form.name.data
        pet.species=form.species.data
        pet.photo_url=form.photo_url.data
        pet.age=form.age.data
        pet.notes=form.notes.data
        pet.available=form.available.data
        db.session.add(pet)
        db.session.commit()     
        category='success'
        msg=f"{pet.name} the {pet.species} had been updated and added to the list of  pets!" 
        flash(msg, category)  
        return redirect('/')
    else:    
        return render_template('edit_pet.html',form=form)
    
