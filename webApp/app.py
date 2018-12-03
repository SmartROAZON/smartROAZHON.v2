import os
import sys
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

with app.test_request_context():
    print(url_for('static', filename='css/style.css'))
    print(url_for('static', filename='css/bootstrap.min.css'))
    print(url_for('static', filename='js/jquery-1.11.1.min.js'))
    print(url_for('static', filename='js/bootstrap.min.js'))
    print(url_for('static', filename='js/searchUI.js'))
    print(url_for('static', filename='img/plus.png'))
    print(url_for('static', filename='img/equal.jpg'))
    print(url_for('static', filename='img/patientez.gif'))
    

@app.route('/user/<username>')
def profile(username):
    print('{}\'s profile'.format(username))
    return home()
	

@app.route('/')
def home(name=None):
    return render_template('drag_n_drop.html', name=name)
	

#################################################
@app.route('/executeScript/<firstCrt>/<secondCrt>')
def executeScript(firstCrt,secondCrt):
	#os.system("python hello.py {0} {1}".format(firstCrt,secondCrt))
	#res=os.popen("python hello.py {0} {1}".format(firstCrt,secondCrt)).readlines()
	res=os.popen("python hello.py {0} {1}".format(firstCrt,secondCrt)).readlines()
	print(res)
	return render_template('results.html',my_string=res)
	
	
@app.route('/criteriaForm')
def criteriaForm():
    return render_template('criteria_specification.html')


@app.route('/drag')
def dragANDdrop(name=None):
    return render_template('drag_n_drop.html', name=name)


if __name__ == '__main__':
    app.run()
