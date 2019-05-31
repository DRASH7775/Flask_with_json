from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, json
app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/',methods=['GET', 'POST'])
def Register_page():
     return render_template('login.html')
 # when enter 127.0.0.1:5000/ directly open login.html

@app.route('/registration', methods=['GET', 'POST'])
def Register_page1():
# when enter 127.0.0.1:5000/registration directly open registration.html

        if request.method == "POST":
            attempted_username = request.form['Username']
            attempted_password = request.form['Password']
            attempted_email= request.form['Email']

            d = {"email": "", "pass": "", "user": ""}
            with open('data.json', 'r') as outfile: 
                data = json.load(outfile)

            print(data)
                # json.load(d, outfile)
            # d = {"email": "", "pass": "", "user": ""}
            d['user']=attempted_username
            
            d['pass']=attempted_password
            
            d['email']=attempted_email
            data.append(d)
            with open('data.json', 'w') as outfile:  
                json.dump(data, outfile, indent=4)

            if request.form['Username'] == '' or request.form['Password'] == '' or request.form['Email'] == '':
               return 'Invalid Credentials. Please try again.' 
            else: 
                return render_template('login.html')
        else:
            return render_template('registration.html')
#--------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    #error = ' '

# try:
    if request.method == "POST":
        # attempted_username = request.form['Username']
        # attempted_password = request.form['Password']
        # attempted_email = request.form['Email']
        
        with open('data.json', 'r') as outfile: 
            data = json.load(outfile)
       
        print(data)
        
        for user in data:
            if request.form['Username'] == user['user'] and request.form['Password'] == user['pass'] and request.form['Email'] == user['email']:
                return 'SUCCESSFULLY LOGGEDIN'
                #error = 'Invalid Credentials. Please try again.'
            # return render_template('bcd.html')
        #return render_template('login.html')

    return "user not found"

@app.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('bcd.html')

if __name__ == '__main__': 
    app.run(debug = True)