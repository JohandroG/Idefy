from idefy_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re


class User:
    def __init__(self,data):
        
        self.first_name = data['first_name']
        self.first_name = data['last_name']
        self.first_name = data['username']
        self.first_name = data['email']
        self.first_name = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#==========================================================================================================

    @classmethod
    def registerUser(cls,data):
        query = "INSERT INTO users (first_name,last_name,username,email,user_password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(username)s,%(email)s,%(encryptedpassword)s,SYSDATE(),SYSDATE())"
        results = connectToMySQL('idefy').query_db(query,data)
        return results

#==========================================================================================================

    @classmethod
    def validatelogin1(cls,loginInfo):
        query = "SELECT * FROM users WHERE email = %(email)s"
        email = {
                "email" : loginInfo,
            }
        results = connectToMySQL('idefy').query_db(query,email)
        return results

    @classmethod
    def validatelogin2(cls,loginInfo):
        query = "SELECT * FROM users WHERE username = %(username)s"
        username = {
                "username" : loginInfo,
            }
        results = connectToMySQL('idefy').query_db(query,username)
        return results

    @classmethod
    def validatelogin3(cls,loginInfo):
        query = "SELECT * FROM users WHERE user_id = %(id)s"
        id = {
                "id" : loginInfo,
            }
        results = connectToMySQL('idefy').query_db(query,id)
        return results

#==========================================================================================================

    @staticmethod
    def registerValidations(data):

        isValid = True

        query = "SELECT * FROM users WHERE email = %(email)s;"
        emaildata = {
                "email" : data['email'],
            }
        results = connectToMySQL('idefy').query_db(query,emaildata)
        


        query = "SELECT * FROM users WHERE username = %(username)s;"
        usernamedata = {
                "username" : data['username'],
            }
        results2 = connectToMySQL('idefy').query_db(query,usernamedata)
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email, write it in a valid format 📝","email")
            isValid=False
        if len(results2) >= 1:
            flash("😥 Username already taken.","username")
            isValid=False
        if len(results) >= 1:
            flash("😥 Email already taken.","email")
            isValid=False
        if len(data['first_name']) < 3:
            flash("The first Name must be at least 3 characters","first_name")
            isValid = False
        if len(data['last_name']) < 3:
            flash("The Last Name must be at least 3 characters","last_name")
            isValid = False
        if len(data['username']) < 3:
            flash("The Username must be at least 3 characters","username")
            isValid = False
        if len(data['password']) < 8:
            flash("The Password must be at least 8 characters","password")
            isValid = False
        if len(data['password']) != len(data['conpass']):
            flash("The Passwords do not match","password")
            isValid = False
        if data['terms'] == False:
            flash("⚠ You need to agree the terms before to continue","general")
            isValid = False

        return isValid


#==========================================================================================================

    @classmethod
    def howmanyPost(cls,id):
        query = "SELECT * FROM idefy_references WHERE user_id = %(id)s"
        results = connectToMySQL('idefy').query_db(query,id)
        return results
    
    @classmethod
    def howmanylikesGiven(cls,id):
        query = "SELECT * FROM idefy_references WHERE liker_id = %(id)s"
        results = connectToMySQL('idefy').query_db(query,id)
        return results
    
    @classmethod
    def howmanylikesReceived(cls,id):
        query = "SELECT SUM(likes) FROM idefy_references LEFT JOIN ideas ON idefy_references.idea_id = ideas.idea_id WHERE user_id = %(id)s"
        results = connectToMySQL('idefy').query_db(query,id)
        return results


#==========================================================================================================
    @classmethod
    def deleteUser(cls,id):

        query = "SELECT user_id,idea_id FROM idefy_references WHERE user_id = %(id)s;"
        results = connectToMySQL('idefy').query_db(query,id)

        # resultInfo = results

        # query1 = "DELETE FROM idefy_references WHERE user_id = %(id)s"
        # result = connectToMySQL('idefy').query_db(query1,id)
        
        # query2 = "DELETE FROM idefy_references WHERE liker_id = %(id)s"
        # result = connectToMySQL('idefy').query_db(query2,id)

        # query = "DELETE FROM users WHERE user_id = %(id)s"
        # result = connectToMySQL('idefy').query_db(query2,id)
        
        # for result in resultInfo:
        #     query = "DELETE FROM ideas WHERE idea_id = %(id)s"
        #     idinfo = {
        #         'id': result['idea_id']
        #     }
        #     result = connectToMySQL('idefy').query_db(query,idinfo)

        

        #=================================In construction==============================================

