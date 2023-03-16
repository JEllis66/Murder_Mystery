from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.characters import Character
from flask_app.models.storyitems import Story_Item
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#GENERAL ROUTES

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin_dashboard')
def admin():
    return render_template('adminDashboard.html')

@app.route('/login',methods=['POST'])
def login():
    if (request.form['login_username'] == "adminlogin"):
        return redirect('/admin_dashboard')
    
    character = Character.get_by_username(request.form)

    if not character or not bcrypt.check_password_hash(character.login_password, request.form['login_password']):
        flash("Login credentails do not match, please check your username spelling or retry entering your password","login")
        return redirect('/')
    session['character_id'] = character.idcharacters
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'character_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['character_id']
    }
    return render_template("dashboard.html",user=Character.get_by_id(data)) #<--- insert default loaded storyitmes here to input into dashboard upon page load

#CREATE

@app.route('/admin_character')
def character_creation():
    return render_template('characterCreation.html')

@app.route('/admin_character_alt')
def character_creation_alt():
    session.pop('login_username', None)
    session.pop('role', None)
    session.pop('relationship', None)
    session.pop('potential_motive', None)
    return render_template('characterCreation.html')

@app.route('/register_character',methods=['POST'])
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
        "potential_motive": request.form['potential_motive'],
    }
    id = Character.save(data)
    session['user_id'] = id

    return redirect('/admin_character_view')

#READ

@app.route('/admin_character_view')
def view_characters():
    return render_template("characterView.html",character=Character.get_all())

#UPDATE

@app.route('/admin_character_edit/<int:id>')
def edit_character(id):
    data = {
        "id" : id
    }
    return render_template("characterEdit.html",character=Character.get_by_id(data))

@app.route('/update/<int:idchar>',methods=['POST'])
def update_character(idchar):
    if not Character.validate_edits(request.form):
        if request.form["login_username"]:
            session['login_username'] = request.form["login_username"]
        if request.form["role"]:
            session['role'] = request.form["role"]
        if request.form["relationship"]:
            session['relationship'] = request.form["relationship"]
        if request.form['potential_motive']:
            session['potential_motive'] = request.form["potential_motive"]
        return redirect('/admin_character_edit/'+str(idchar))
    data = { 
        "idcharacters": idchar,
        "login_username": request.form['login_username'],
        "role": request.form['role'],
        "relationship": request.form['relationship'],
        "potential_motive": request.form['potential_motive'],
    }
    Character.update(data)
    return redirect('/admin_character_view')

#DELETE

@app.route('/admin_character_clear')
def go_nuclear():
    Character.nuke()
    return redirect('/admin_character_view')


@app.route('/admin_character_delete/<int:idchar>')
def delete_one(idchar):
    data = {
        "idcharacters": idchar
    }
    Character.delete_one(data)
    return redirect('/admin_character_view')