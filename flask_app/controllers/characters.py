from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.characters import Character
from flask_app.models.storyitems import Story_Item
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/register',methods=['POST'])
def register():

    if not Character.validate_register(request.form):
        return redirect('/')
    data = { 
        "login_username": request.form['login_username'],
        "login_password": bcrypt.generate_password_hash(request.form['login_password']),
        "role": request.form['role'],
        "relationship": request.form['relationship'],
        "potential_motive": request.form['potential_motiove'],
    }
    id = Character.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    character = Character.get_by_username(request.form)

    if not character or not bcrypt.check_password_hash(character.login_password, request.form['login_password']):
        flash("Login credentails do not match","login")
        return redirect('/')
    session['user_id'] = character.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'character_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['character_id']
    }
    return render_template("dashboard.html",user=Character.get_by_id(data),storyitems=Story_Items.get_all()) #<--- insert default loaded storyitmes here to input into dashboard upon page load

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')