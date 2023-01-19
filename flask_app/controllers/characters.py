from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.characters import Character
from flask_app.models.storyitems import Story_Item
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin_dashboard')
def admin():
    return render_template('adminDashboard.html')

@app.route('/admin_character')
def character_creation():
    return render_template('characterCreation.html')

@app.route('/admin_character_refresh')
def character_refresh():
    session.pop('login_username', None)
    session.pop('role', None)
    session.pop('relationship', None)
    session.pop('potential_motive', None)
    return render_template('characterCreation.html')

@app.route('/admin_item')
def item_creation():
    return render_template('storyItemCreation.html')

@app.route('/register',methods=['POST'])
def register():

    if not Character.validate_register(request.form):
        if request.form["login_username"]:
            session['login_username'] = request.form["login_username"]
        if request.form["role"]:
            session['role'] = request.form["role"]
        if request.form["relationship"]:
            session['relationship'] = request.form["relationship"]
        if request.form['potential_motive']:
            session['potential_motive'] = request.form["potential_motive"]
        return redirect('/admin_character')
    data = { 
        "login_username": request.form['login_username'],
        "login_password": bcrypt.generate_password_hash(request.form['login_password']),
        "character_name": request.form['login_username'],
        "role": request.form['role'],
        "relationship": request.form['relationship'],
        "potential_motive": request.form['potential_motiove'],
    }
    id = Character.save(data)
    session['user_id'] = id

    return redirect('/admin_dashboard')

@app.route('/login',methods=['POST'])
def login():
    character = Character.get_by_username(request.form)

    if (request.form['login_username'] == "adminlogin"):
        return redirect('/admin_dashboard')

    if not character or not bcrypt.check_password_hash(character.login_password, request.form['login_password']):
        flash("Login credentails do not match, please check your username spelling or retry entering your password","login")
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