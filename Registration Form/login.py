#this is currently not in use i have directly add this to reigister.py 
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, json
app = Flask(__name__)
app.secret_key = "super secret key"

# @app.route('/')
# def home_page():
#     return render_template("main.html")

@app.route('/', methods=['GET', 'POST'])
def login_page():
    #error = ' '

# try:

    if request.method == "POST":
        attempted_username = request.form['Username']
        attempted_password = request.form['Password']
        attempted_email = request.form['Email']
        
        d = {}
        with open('data.txt', 'r') as outfile:  
            json.load(d, outfile)
            
            d['user']=attempted_username
            d['pass']=attempted_password
            d['email']=attempted_email

        if request.form['Username'] == d['user'] and request.form['Password'] == d['pass'] and request.form['Email'] == d['email']:
           #return 'SUCCESSFULLY LOGGEDIN'
                #error = 'Invalid Credentials. Please try again.'
            return render_template('bcd.html')
        else:
            return 'invalid '
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)




        # flash(attempted_username)
        # flash(attempted_password)

        # if attempted_username == "drashti" and attempted_password == "123456":
        #     return redirect(url_for('home_page'))
        # else:
        #     error = "Invalid credentials . Try it again."
        #     return render_template("login.html", error = error)

# except Exception as e:
        # flash(e)
        # print(e)

    # return render_template("login.html")

# @app.route('/Register/', methods=['GET', 'POST'])
# def Register_page():
#     error = ''
# # try:
#     if request.method == "POST":
#         attempted_username = request.form['Username']
#         attempted_password = request.form['Password']
#         attempted_email= request.form['Email']
        
#         flash(attempted_username)
#         flash(attempted_password)
#         flash(attempted_email)

#         d = {}
#         d['user']=attempted_username
#         d['pass']=attempted_password
#         d['email']=attempted_email
#         with open('data.txt', 'a') as outfile:  
#             json.dump(d, outfile)


        # if (attempted_username == "drashti" and attempted_password == "123456" and attempted_password == "panchaldrashti7775@gmail.com"):
        #     return redirect(url_for('login_page'))
        # else:
        #     error = "Invalid credentials . Try it again."
        #     return render_template("registration.html", error = error)

# except Exception as e:
        # flash(e)
        # print(e)

    # return render_template("registration.html")

