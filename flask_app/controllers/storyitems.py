from readline import redisplay
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.storyitems import Story_Item
from flask_app.models.characters import Character

#CREATE
@app.route('/new/story_item')
def new_story_item():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('storyItemCreation.html',user=Character.get_by_id(data))

@app.route('/create/story_item',methods=['POST'])
def create_story_item():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Story_Item.validate_tv_show(request.form):
        return redirect('/new/story_item')
    data = {
        "story_title": request.form["story_title"],
        "description": request.form["description"],
        "lookup_key": request.form["lookup_key"],
        "storyitemscol": request.form["storyitemscol"],
        "item_content": request.form["item_content"],
        "user_id": session["user_id"]
    }
    Story_Item.save(data)
    return redirect('/dashboard')

#READ
@app.route('/story_item/<int:id>')
def show_story_item(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_story_item.html",stroy_item=Story_Item.get_one(data),user=Character.get_by_id(user_data))

#UPDATE
@app.route('/edit/story_item/<int:id>')
def edit_story_item(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_story_item.html",edit=Story_Item.get_one(data),user=Character.get_by_id(user_data))

@app.route('/update/story_item',methods=['POST'])
def update_story_item():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Character.validate_story_item(request.form):
        return redirect('/edit/story_item/' + str(Story_Item.get_one(request.form).id))
    data = {
        "story_title": request.form["story_title"],
        "description": request.form["description"],
        "lookup_key": request.form["lookup_key"],
        "storyitemscol": request.form["storyitemscol"],
        "item_content": request.form["item_content"],
        "user_id": session["user_id"]
    }
    Story_Item.update(data)
    return redirect('/dashboard')

#DELETE
@app.route('/destroy/story_item/<int:id>')
def destroy_story_item(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Story_Item.destroy(data)
    return redirect('/dashboard')