from idefy_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

class Category:
    def __init__(self,data):
        
        self.category_id = data['category_id']
        self.category = data['category']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#==========================================================================================================
    @classmethod
    def getcategoryID(cls,data):

        query = "SELECT category_id FROM categories WHERE category = %(category)s"

        info = {
            'category' : data
        }

        results = connectToMySQL('idefy').query_db(query,info)
        actualCategoryID = results[0]['category_id']
        return actualCategoryID


#==========================================================================================================

    @classmethod
    def addcategory(cls,data):
        query = "INSERT INTO categories (category,created_at,updated_at) VALUES (%(category)s,SYSDATE(),SYSDATE())"
        results = connectToMySQL('idefy').query_db(query,data)
        return results


    @classmethod
    def getcategories(cls):
        query = "SELECT * FROM categories"
        results = connectToMySQL('idefy').query_db(query)
        return results


    @staticmethod
    def categoryValidations(data):
        
        isValid = True

        query = "SELECT * FROM categories WHERE category = %(category)s;"
        results = connectToMySQL('idefy').query_db(query,data)

        CAT_REGEX = re.compile(r'^@+[a-z+_-]+$')


        if len(results) >= 1:
            flash("😪 This category already exits")
            isValid=False
        if not CAT_REGEX.match(data['category']):
            flash("📝 Please follow the format to create a category. EX: @category")
            isValid=False
        return isValid

#==========================================================================================================

    @classmethod
    def deletecategory(cls,data):
        query = "DELETE FROM categories WHERE category = %(category)s"
        results = connectToMySQL('idefy').query_db(query,data)
        return results