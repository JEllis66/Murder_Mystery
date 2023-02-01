from readline import redisplay
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.storyitems import Story_Item
from flask_app.models.characters import Character

#MISC

@app.route('/admin_item')
def item_creation():
    myApiKey = "1218e00a-76a4-4c26-a211-487c4d8e041d"
    return render_template('storyItemCreation.html',apiKey = myApiKey)

@app.route('/admin_story_refresh')
def story_refresh():
    myApiKey = "1218e00a-76a4-4c26-a211-487c4d8e041d"
    session.pop('story_title', None)
    session.pop('description', None)
    session.pop('lookup_key', None)
    session.pop('item_content', None)
    return render_template('storyItemCreation.html',apiKey = myApiKey)

#CREATE

# @app.route('/new/story_item')
# def new_story_item():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":session['user_id']
#     }
#     return render_template('storyItemCreation.html',user=Character.get_by_id(data))

@app.route('/create/story_item',methods=['POST'])
def create_story_item():
    myApiKey = "1218e00a-76a4-4c26-a211-487c4d8e041d"
    if not Story_Item.validate_story_item(request.form):
        if request.form["story_title"]:
            session['story_title'] = request.form["story_title"]
        if request.form["description"]:
            session['description'] = request.form["description"]
        if request.form["lookup_key"]:
            session['lookup_key'] = request.form["lookup_key"]
        return render_template('storyItemCreation.html',apiKey = myApiKey)
    data = {
        "story_title": request.form["story_title"],
        "description": request.form["description"],
        "lookup_key": request.form["lookup_key"],
        "item_content": request.form["item_content"]
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
    return render_template("show_story_item.html",stroy_item=Story_Item.get_one(data),user=Character.get_by_id(user_data["id"]))


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
        "item_content": request.form["item_content"]
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