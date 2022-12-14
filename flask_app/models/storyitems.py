from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import storyitems


class Story_Item:
    db_name = 'story_items'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.story_title = db_data['story_title']
        self.description = db_data['description']
        self.lookup_key = db_data['lookup_key']
        self.storyitemscol = db_data['storyitemscol']
        self.item_content = db_data['item_content']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # self.user_id = db_data['user_id']
        # self.reporter = []


#CREATE
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO story_items (story_title, description, lookup_key, description, storyitemscol, item_content) 
        VALUES (%(story_title)s,%(description)s,%(lookup_key)s,%(description)s,%(storyitemscol)s,%(item_content)s)
        ;"""
        return connectToMySQL(cls.db_name).query_db(query, data)

#READ
    @classmethod
    def get_all(cls):
        query = """
        SELECT * 
        FROM story_items
        ;"""
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_story_items = []
        for row in results:
            all_story_items.append( cls(row) )
        return all_story_items
    
    @classmethod
    def get_one(cls,data):
        # query = """
        # SELECT * 
        # FROM story_items 
        # WHERE id = %(id)s
        # ;"""
        # results = connectToMySQL(cls.db_name).query_db(query,data)
        # return cls( results[0] )
        query = """
        SELECT *
        FROM story_items
        WHERE story_items.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db_name).query_db(query, data)
        this_story_item = cls(results[0])                                         
        # for story in results:
        #     data = {
        #         'story_title' : story['story_title'],
        #         'description' : story['description'],
        #         'lookup_key' : story['lookup_key'],
        #         'storyitemscol' : story['storyitemcol'],
        #         'item_content' : story['item_content'],
        #         'created_at' : story['created_at'],
        #         'updated_at' : story['updated_at'],
        #         'id' : story['users.id']
        #     }
        #     # this_story_item.append(user.User(story))
        return this_story_item
        
# STOPPED HERE 12/14/2022 <---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#UPDATE
    @classmethod
    def update(cls, data):
        query = """
        UPDATE story_items SET story_title=%(story_title)s, description=%(description)s, lookup_key=%(lookup_key)s, storyitemscol=%(storyitemscol)s, item_content=%(item_content)s,  updated_at=NOW() WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db_name).query_db(query,data)
    
#DELETE    
    @classmethod
    def destroy(cls,data):
        query = """
        DELETE FROM story_items 
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db_name).query_db(query,data)




    @staticmethod
    def validate_story_item(story_item):
        is_valid = True
        if len(story_item['story_title']) < 5:
            is_valid = False
            flash("Title of story must be at least 5 characters long","story_item")
        if len(story_item['description']) < 8:
            is_valid = False
            flash("Description of the story item must be at least 8 characters long","story_item")
        if len(story_item['lookup_key']) < 8 :
            is_valid = False
            flash("Lookup keys should be at least 8 characters so they're not too easy to guess, you silly goose!","story_item")
        if len(story_item['storyitemscol']) < 3:
            is_valid = False
            flash("Storyitemscol must be at least 3 characters in length","story_item")
        if len(story_item['storyitemscol']) < 2:
            is_valid = False
            flash("Item Content column must be at least 2 characters in length","story_item")
        return is_valid