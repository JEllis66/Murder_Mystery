from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash
from flask_app.models import storyitems

class Character:
    db_name = "lancasters_schema"
    def __init__(self,data):
        self.id = data['id']
        self.login_username = data['login_username']
        self.login_password = data['login_password']
        self.role = data['role']
        self.character_name = data['login_username']
        self.relationship = data['relationship']
        self.potential_motive = data['potential_motive']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#CREATE
    @classmethod
    def save(cls,data):
        query = "INSERT INTO characters (login_username,login_password,role,relationship,potential_motive) VALUES(%(login_username)s,%(login_password)s,%(role)s,%(relationship)s,%(potential_motive)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)

#READ
    @classmethod
    def get_all(cls):
        query = """
        SELECT * 
        FROM characters
        ;"""
        results = connectToMySQL(cls.db_name).query_db(query)
        characters = []
        for row in results:
            characters.append( cls(row))
        return characters

    @classmethod
    def get_by_username(cls,data):
        query = """
        SELECT * 
        FROM characters
        WHERE login_username = %(login_username)s
        ;"""
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM characters WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

        # query = """
        # SELECT *
        # FROM users
        # LEFT JOIN tv_shows
        # ON users.id = tv_shows.user_id
        # WHERE users.id = %(id)s
        # ;"""
        # results = connectToMySQL(cls.db_name).query_db(query, data)
        # this_user = cls(results[0])                                         
        # for show in results:
        #     data = {
        #         'title' : show['title'],
        #         'network' : show['network'],
        #         'release_date' : show['release_date'],
        #         'created_at' : show['tv_shows.created_at'],
        #         'updated_at' : show['tv_shows.updated_at'],
        #         'id' : show['tv_shows.id']
        #     }
        #     this_user.shows.append(tv_show.Tv_show(show))
        # return this_user

            
    @staticmethod
    def validate_register(character):
        is_valid = True
        query = """
        SELECT * FROM characters WHERE login_username = %(login_username)s
        ;"""
        results = connectToMySQL(Character.db_name).query_db(query,character)
        if len(results) >= 1:
            flash("Username has already been used.","register")
            is_valid=False
        # if not EMAIL_REGEX.match(character['email']):
        #     flash("Invalid Email!","register")
        #     is_valid=False
        if len(character['login_username']) < 2:
            flash("First name must be at least 2 characters","register")
            is_valid= False
        if len(character['login_password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if character['login_password'] != character['confirm_password']:
            flash("'Password' and 'Confirm Password' must match","register")
        if len(character['role']) < 2:
            flash("Role description must be at least 2 characters","register")
            is_valid= False
        if len(character['relationship']) < 3:
            flash("The character's relationship must be described with at least 3 characters, but probably more","register")
            is_valid= False
        if len(character['potential_motive']) < 8:
            flash("Potential Motive for Murder must be at least 8 characters","register")
            is_valid= False
        # if user['password'] != user['confirm']:
        #     flash("Passwords must match","register")
        return is_valid