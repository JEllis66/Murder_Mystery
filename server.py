from flask_app import app
from flask_app.controllers import characters,characters_has_storyitems,storyitems

if __name__=="main":
    app.run(debug=True)
