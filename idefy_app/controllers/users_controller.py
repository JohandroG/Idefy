import re
from flask import render_template, session, redirect, request
from idefy_app import app
from idefy_app.models.user import User
from idefy_app.models.category import Category
from idefy_app.models.idea import Idea
from flask_bcrypt import Bcrypt
from flask import flash


bcrypt = Bcrypt(app)

# ==================================================Display pages===========================================

@app.route('/', methods = ['GET'])
def displayindexinfo():
    
    return render_template('index.html')

@app.route('/register', methods = ['GET'])
def displayRegisterinfo():
    
    return render_template('register.html')

@app.route('/login', methods = ['GET'])
def displayLogininfo():
    
    return render_template('login.html')

@app.route('/dashboard', methods = ['GET'])
def displayDashboardinfo():
    
    userInfo = session['user_info']
    categoriesInfo = Category.getcategories()
    ideasInfo = Idea.displayIdeasAllinfo()
    
    

    return render_template('dashboard.html', user = userInfo, categories = categoriesInfo, ideas = ideasInfo)

@app.route('/profile/<int:id>', methods = ['GET'])
def displayProfileinfo(id):

    userInfo = User.validatelogin3(id)
    
    idData = {
        "id" : id,
    }
    
    

    postInfo = User.howmanyPost(idData)
    likesGInfo = User.howmanylikesGiven(idData)
    likesRInfo = User.howmanylikesReceived(idData)

    if likesRInfo[0]['SUM(likes)'] == None:
        likesRInfoC = 0
    else:
        likesRInfoC = likesRInfo[0]['SUM(likes)']


    return render_template ('profile.html', user = userInfo[0], userSession = session['user_info'] , ideas = len(postInfo), likesG = len(likesGInfo), likesR = likesRInfoC)


# ==================================================Login and register controllers===========================================

@app.route('/register/submit', methods = ['POST'])
def submitReg():

    firstName = request.form['first_name']
    lastName = request.form['last_name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirmPass = request.form['conpass']

    if "terms" not in request.form:
        termsagree = False
    else:
        termsagree = request.form['terms']


    if password == "":
        flash("You need to create a password before to continue 🔑","password")
        return redirect('/register')
    else:
        encryptedpassword = bcrypt.generate_password_hash(password)

        newUserInfo = {
            "first_name" : firstName,
            "last_name" : lastName,
            "username" : username,
            "email" : email,
            "password" : password,
            "encryptedpassword" : encryptedpassword,
            "conpass" : confirmPass,
            "terms" : termsagree 
        }

        if User.registerValidations(newUserInfo):
            result = User.registerUser(newUserInfo)
            userinfo = User.validatelogin3(result)
            session.clear()
            user_info = userinfo[0]
            session['user_info'] = user_info
            return redirect('/dashboard')
        else:
            return redirect('/register')

@app.route ('/login/submit', methods = ['POST'])
def loginValidation():
    emailorUsername = request.form['emailUser']
    password = request.form['user_password']
    
    result = User.validatelogin1(emailorUsername)

    if len(result) == 1:
        encryptedPassword = result[0]['user_password']
        if bcrypt.check_password_hash(encryptedPassword,password):
            session.clear()
            user_info = result[0]
            session['user_info'] = user_info
            return redirect ('/dashboard')
        else:
            flash("You entered the wrong password for this Email 😓","password")
    elif len(result) == 0:
        result2 = User.validatelogin2(emailorUsername)
        if len(result2) == 1:
            encryptedPassword = result2[0]['user_password']
            if bcrypt.check_password_hash(encryptedPassword,password):
                session.clear()
                user_info = result2[0]
                session['user_info'] = user_info
                return redirect ('/dashboard')
            else:
                flash("You entered the wrong password for this Username 😓","password")
        else:
            flash("There is no user with this information 📃❌","login")


    return redirect('/login')

# ==================================================Logout and clean session===========================================
@app.route('/delete/user', methods = ['POST'])
def deleteUser():

    user_id = request.form['id']

    idDict = {
        'id' : user_id
    }

    info = User.deleteUser(idDict)
    
    print(info)
    print(info)
    print(info)

    return redirect('/logout')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')






