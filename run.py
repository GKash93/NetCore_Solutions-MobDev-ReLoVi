#!/usr/bin/env python
#-----------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for
import functions
app = Flask(__name__)
#------------------------------------------------------------------------------
#Establish a route to Login Page
@app.route('/login', methods = ['GET'])
def login():
    if request.method == 'POST':
        username = ''
	password = ''
	if username == 'admin' and password == 'pas123':
	     redirect(url_for('rlv_page.html'))
	else:
	    redirect(url_for('login.html'))

    return render_template("login.html")
#------------------------------------------------------------------------------
#Establish a route to Remote Log Viewer page		
@app.route('/rlv', methods = ["GET","POST"])
def rlv():
    return render_template('rlv_page.html', f = functions)
  
#---------------------------------------------------------------------------------
if __name__ == '__main__':
	app.run(debug = True)

