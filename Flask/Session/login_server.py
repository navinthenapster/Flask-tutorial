from flask import Flask, flash, redirect, render_template, request, url_for,make_response
import datetime

app = Flask(__name__,static_folder='static',template_folder='static')
app.secret_key = 'random string'

@app.route('/')
def index():
   return render_template('index.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
	 
	 resp = make_response(redirect(url_for('user')))
	 expire_date = datetime.datetime.now()
	 expire_date = expire_date + datetime.timedelta(days=1)
	 resp.set_cookie('userID', request.form['username'],max_age=10,expires=expire_date)
         return resp
			
   return render_template('login.html', error = error)

@app.route('/user')
def user():
   name = "admin"
   name=request.cookies.get('userID')
   if name : 
   	return '<h1>welcome '+name+'</h1> <br> <a href="/logout"> logout </a>'
   return "UnAuthorized : Forbidden "

@app.route('/logout')
def logout():
    try:
	if request.cookies.get('userID'):
    		request.cookies.pop('userID', None)
    except :
    	pass 
    return redirect(url_for('index')) 



if __name__ == "__main__":
   app.run(debug = True)
