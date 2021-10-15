import re
from flask import render_template, session, redirect, request
from flask.scaffold import F
from idefy_app import app
from idefy_app.models.user import User
from idefy_app.models.category import Category
from idefy_app.models.idea import Idea
from flask_bcrypt import Bcrypt
from flask import flash

# ==================================================Display pages===========================================

@app.route('/category', methods = ['GET'])
def displayCategoryform():
    
    categoryes = Category.getcategories()
    userInfo = session['user_info']
    ideasInfo = Idea.displayIdeasAllinfo()
    
    return render_template('addcategory.html', categories = categoryes, user = userInfo, ideas = ideasInfo)

    


# ==================================================Add and validate categories===========================================

@app.route('/add/category', methods = ['POST'])
def addCat():

    categoryinfo = {
    'category' : request.form['category']
    }

    if Category.categoryValidations(categoryinfo):
        Category.addcategory(categoryinfo)
        flash('Category created successfully 😀')

    return redirect('/category')


@app.route('/delete/category', methods = ['POST'])
def deleteCat():

    categoryname = request.form['categorydel']
    cat = {
        'category' : categoryname
    }
    result = Category.deletecategory(cat)
    
    if result == False:
        flash('Somebody is using this category you can not delete it 😅')
    elif result == None:
        flash('Category deleted successfully ✅')

    return redirect ('/category')


# ================================================== Filter ===========================================

@app.route('/dashboard/filtered', methods = ['POST'])
def filterCat():

    categoryfil = request.form['categoryfil']

    info = {
        "category" : categoryfil
    }

    filteredIdeas = Idea.displayFilteredinfo(info)
    userInfo = session['user_info']
    categoriesInfo = Category.getcategories()


    return render_template ('dashboard.html', user = userInfo, categories = categoriesInfo, ideas = filteredIdeas)