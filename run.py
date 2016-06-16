#!/usr/bin/env python
#-----------------------------------------------------------------------------
#flask library and import modules
from flask import Flask, render_template, request, redirect, url_for
#import the .py extensions
import functions, os
#an instance of flask class and __name__ is used for single module
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
#------------------------------------------------------------------------------
#Establish a route to Login Page
@app.route('/login', methods = ['GET'])
def login():
     username = request.args.get('Username')
     password = request.args.get('Password')
     print username
     print password
     print request.method
     if request.method == 'GET':
         if username == 'admin' and password == '123':
	      print "Yes"
	      return redirect(url_for('rlv'))
	 else:
	      render_template('login.html')
     return render_template('login.html')
#------------------------------------------------------------------------------
#Establish a route to Remote Log Viewer page		
@app.route('/rlv', methods = ["GET","POST"])
def rlv():
    log = request.args.get('log_file')   # Read Log File
    print "LogFile Selected: ",log
    Hwrd = request.args.get('Sel1')   # Read the WORD
    print "Search having the word:", Hwrd
    fd = request.args.get('frm_dt')
    print "From Date", fd
    td = request.args.get('to_dt')
    print "To-Date", td
    result = ''
    if log and log != '-1':
	command = "python /home/ganesh/remote_log_viewer/remote_log_viewer.py %s %s %s %s" % (log,fd,td,Hwrd)
        print command
        result = functions.salt_exec(command)
        print result

    return render_template('rlv_page.html', f = functions, r = result)
#---------------------------------------------------------------------------------
if __name__ == '__main__':
	app.run(debug = True)
