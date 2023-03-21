from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import storyitems, characters


class Story_Item:
    db_name = 'lancasters_schema'
    def __init__(self,db_data):
        self.idstoryitems = db_data['idstoryitems']
        self.story_title = db_data['story_title']
        self.description = db_data['description']
        self.lookup_key = db_data['lookup_key']
        self.item_content = db_data['item_content']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # self.user_id = db_data['user_id']
        # self.reporter = []


#CREATE
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO storyitems (story_title, description, lookup_key, item_content) 
        VALUES (%(story_title)s,%(description)s,%(lookup_key)s,%(item_content)s)
        ;"""
        return connectToMySQL(cls.db_name).query_db(query, data)

#READ
    @classmethod
    def get_all_storyitems(cls):
        query = """
        SELECT * 
            FROM storyitems
        ;"""
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_storyitems = []
        for row in results:
            all_storyitems.append( cls(row) )
        return all_storyitems
    
    @classmethod
    def get_storyitem_by_id(cls,data):
        query = """
        SELECT *
            FROM storyitems
            WHERE idstoryitems = %(idstoryitems)s
        ;"""
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results                                         

#UPDATE
    @classmethod #had story['columnnamehere'] on lines 57-60
    def update_si(cls, data):
        query = """
            UPDATE storyitems SET
                'story_title' : storyitem['story_title'], 
                'description' : storyitem['description'],
                'lookup_key' : storyitem['lookup_key'],
                'item_content' : storyitem['item_content'],
            WHERE idstoryitems = %(idstoryitems)s
        ;"""
        return connectToMySQL(cls.db_name).query_db(query,data)
    
#DELETE    
    @classmethod
    def delete_one_si(cls,data):
        query = """
        DELETE FROM storyitems 
        WHERE idstoryitems = %(idstoryitems)s
        ;"""
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def post(cls,data):
        query = """
            DELETE * FROM storyitems
        ;"""
        return connectToMySQL(cls.db_name).query_db(query,data)


    @staticmethod
    def validate_storyitem(storyitem):
        is_valid = True
        if len(storyitem['story_title']) < 5:
            is_valid = False
            flash("Title of story must be at least 5 characters long","story_item")
        if len(storyitem['description']) < 8:
            is_valid = False
            flash("Description of the story item must be at least 8 characters long","story_item")
        if len(storyitem['lookup_key']) < 8 :
            is_valid = False
            flash("Lookup keys should be at least 8 characters so they're not too easy to guess, you silly goose!","story_item")
        if not storyitem['item_content']:
            is_valid = False
            flash("You must include item content","story_item")
        return is_valid
    
    @staticmethod
    def validate_storyitem_edits(storyitem):
        is_valid = True
        query = """
            SELECT * FROM storyitems 
            WHERE idstoryitems = %(idstoryitems)s
        ;"""
        results = connectToMySQL(Story_Item.db_name).query_db(query,storyitem)
        if len(storyitem['story_title']) < 5:
            is_valid = False
            flash("Title of story must be at least 5 characters long","story_item")
        if len(storyitem['description']) < 8:
            is_valid = False
            flash("Description of the story item must be at least 8 characters long","story_item")
        if len(storyitem['lookup_key']) < 8 :
            is_valid = False
            flash("Lookup keys should be at least 8 characters so they're not too easy to guess, you silly goose!","story_item")
        if not storyitem['item_content']:
            is_valid = False
            flash("You must include item content","story_item")
        return is_valid