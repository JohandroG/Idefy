from idefy_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

class Idea:
    def __init__(self,data):
        
        self.idea_id = data['idea_id']
        self.idea_info = data['idea_info']
        self.likes = data['likes']
        self.category = data['category']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#==========================================================================================================

    @classmethod
    def addMSJ(cls,data):
        query = "INSERT INTO ideas (idea_info, likes, category, created_at, updated_at) VALUES (%(idea)s,0,%(category)s,SYSDATE(),SYSDATE());"

        info = {
            'idea' : data[0],
            'category' : data[1]
        }

        results = connectToMySQL('idefy').query_db(query,info)
        return results

    @classmethod
    def linkInfo(cls,data):
        query = "INSERT INTO idefy_references (user_id, idea_id, category_id) VALUES (%(user_id)s,%(idea_id)s,%(category_id)s);"
        
        info = {
            'user_id' : data[0],
            'idea_id' : data[1],
            'category_id' : data[2]
        }

        results = connectToMySQL('idefy').query_db(query,info)
        return results

#==========================================================================================================

    @classmethod
    def displayIdeasAllinfo(cls):
        query = "SELECT * FROM idefy_references LEFT JOIN users ON idefy_references.user_id = users.user_id LEFT JOIN ideas ON idefy_references.idea_id = ideas.idea_id;"
        results = connectToMySQL('idefy').query_db(query)
        return results

#==========================================================================================================

    @classmethod
    def like(cls,data):

        query = "UPDATE ideas SET likes = likes + 1 WHERE idea_id = %(idea_id)s;"
        results = connectToMySQL('idefy').query_db(query,data)
    
    @classmethod
    def dislike(cls,data):

        query = "UPDATE ideas SET likes = likes - 1 WHERE idea_id = %(idea_id)s;"
        results = connectToMySQL('idefy').query_db(query,data)

#==========================================================================================================
    @classmethod
    def coincidence(cls,data):

        query = "SELECT * FROM idefy_references WHERE liker_id = %(liker_id)s and idea_id = %(idea_id)s"
        results = connectToMySQL('idefy').query_db(query,data)
        return results

#==========================================================================================================

    @classmethod
    def insertLike(cls,data):
        query = "INSERT INTO idefy_references (idea_id,liker_id) VALUES (%(idea_id)s,%(liker_id)s);"
        results = connectToMySQL('idefy').query_db(query,data)
    
    @classmethod
    def removeLike(cls,data):
        query = "DELETE FROM idefy_references WHERE liker_id = %(liker_id)s AND idea_id = %(idea_id)s"
        results = connectToMySQL('idefy').query_db(query,data)

#==========================================================================================================
    @classmethod
    def whoLikes(cls,data):
        query = "SELECT * FROM idefy_references LEFT JOIN users ON idefy_references.liker_id = users.user_id WHERE idea_id = %(idea_id)s"
        results = connectToMySQL('idefy').query_db(query,data)
        return results

#==========================================================================================================
    @classmethod
    def deleteIdea(cls,data):
        query = "DELETE FROM idefy_references WHERE idea_id = %(id)s"
        results = connectToMySQL('idefy').query_db(query,data)
        
        query = "DELETE FROM ideas WHERE idea_id = %(id)s"
        results2 = connectToMySQL('idefy').query_db(query,data)

#==========================================================================================================

    @classmethod
    def editIdeas(cls,data):
        query = "UPDATE ideas SET idea_info = %(idea)s, category = %(category)s WHERE idea_id = %(id)s"
        results = connectToMySQL('idefy').query_db(query,data)
        return results

    @classmethod
    def displayFilteredinfo(cls,data):
        query = "SELECT * FROM idefy_references LEFT JOIN users ON idefy_references.user_id = users.user_id LEFT JOIN ideas ON idefy_references.idea_id = ideas.idea_id WHERE category =%(category)s;"
        results = connectToMySQL('idefy').query_db(query,data)
        return results
    


