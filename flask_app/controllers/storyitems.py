from readline import redisplay
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.storyitems import Story_Item
from flask_app.models.characters import Character

#CREATE

@app.route('/admin_item')
def item_creation():
    myApiKey = "1218e00a-76a4-4c26-a211-487c4d8e041d"
    return render_template('storyItemCreation.html',apiKey = myApiKey)

@app.route('/admin_story_alt')
def story_refresh():
    myApiKey = "1218e00a-76a4-4c26-a211-487c4d8e041d"
    session.pop('story_title', None)
    session.pop('description', None)
    session.pop('lookup_key', None)
    session.pop('item_content', None)
    return render_template('storyItemCreation.html',apiKey = myApiKey)

@app.route('/register_story_item',methods=['POST'])
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

@app.route('/story_item_view')
def view_story_items():
    return render_template("storyItemView.html",story_item=Story_Item.get_all())

@app.route('/admin_story_item_view/<int:id>')
def view_story_item(id):
    data = {
        "id" : id
    }
    return render_template("characterEdit.html",story_item=Story_Item.get_by_id(data))

#good starting place for viewing a character's list of their specific item(s)/story(ies)
# @app.route('/story_item/<int:id>')
# def show_story_item(id):
#     data = {
#         "id":id
#     }
#     char_data = {
#         "id":session['user_id']
#     }
#     return render_template("show_story_item.html",stroy_item=Story_Item.get_one(data),user=Character.get_by_id(user_data["id"]))


#UPDATE
@app.route('/admin_story_item_edit/<int:id>')
def edit_story_item(id):
    data = {
        "id":id
    }
    return render_template("edit_story_item.html",edit=Story_Item.get_by_id(data))

@app.route('/update/<int:idstor>',methods=['POST'])
def update_story_item(idstor):
    if not Character.validate_story_item_edits(request.form):
        if request.form["story_title"]:
                session['story_title'] = request.form["story_title"]
        if request.form["description"]:
            session['description'] = request.form["description"]
        if request.form["lookup_key"]:
            session['lookup_key'] = request.form["lookup_key"]
        if request.form['item_content']:
            session['item_content'] = request.form["item_content"]
        return redirect('/admin_story_item_edit/'+str(idstor))
    data = {
        "story_title": request.form["story_title"],
        "description": request.form["description"],
        "lookup_key": request.form["lookup_key"],
        "item_content": request.form["item_content"]
    }
    Story_Item.update(data)
    return redirect('/admin_stroy_item_view')

#DELETE
@app.route('/admin_character_clear')
def go_postal():
    Character.post()
    return redirect('/admin_character_view')


@app.route('/admin_character_delete/<int:idchar>')
def delete_one_story_item(idstor):
    data = {
        "idstoryitems": idstor
    }
    Character.delete_one_story_item(data)
    return redirect('/admin_stroy_item_view')