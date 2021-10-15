import re
from flask import render_template, session, redirect, request
from idefy_app import app
from idefy_app.models.user import User
from idefy_app.models.category import Category
from idefy_app.models.idea import Idea
from flask_bcrypt import Bcrypt
from flask import flash


# ==================================================Display pages===========================================
@app.route('/who/like/<int:id>', methods = ['GET'])
def showWhoLikes(id):
    idInfo = {
        'idea_id': id
    }

    likesinfo = Idea.whoLikes(idInfo)

    return render_template('likes.html', likes = likesinfo)

# ==================================================Add ideas and others===========================================


@app.route('/add/idea', methods = ['POST'])
def addIdeas():


# =================validations are pending ====================

    idea = request.form['idea']
    category = request.form['category']
    user_id = request.form['user_id']
    category_id = Category.getcategoryID(category)
    
    
    ideaInfo1 = (idea,category)
    add_and_idea_id = Idea.addMSJ(ideaInfo1)

    ideaInfo2 = (user_id,add_and_idea_id,category_id)
    Idea.linkInfo(ideaInfo2)

    return redirect ('/dashboard')

# ==================================================likes===========================================

@app.route('/like/<int:id>', methods = ['GET'])
def addLikes(id):

    idsInfo = {
        "liker_id" : session['user_info']['user_id'],
        "idea_id" : id
    }

    
    coincidence =Idea.coincidence(idsInfo)

    

    if len(coincidence) > 0:
        Idea.dislike(idsInfo)
        Idea.removeLike(idsInfo)
    else:
        Idea.like(idsInfo)
        Idea.insertLike(idsInfo)

    return redirect('/dashboard') #=========Nesecito algo que no me recargue la pagina


@app.route('/delete/<int:id>', methods = ['GET'])
def deleteIdea(id):

    idDic = {
        'id' : id
    }
    Idea.deleteIdea(idDic)

    return redirect ('/dashboard')


@app.route('/edit/<int:id>', methods = ['POST'])
def editIdea(id):
    
    category = request.form['categoryedit']
    info = request.form['edit']
    
    info = {
        'id' : id,
        'idea' : info,
        'category' : category
    }
        
    Idea.editIdeas(info)

    return redirect('/dashboard') #=========Nesecito algo que no me recargue la pagina
