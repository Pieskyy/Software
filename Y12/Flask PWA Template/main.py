from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/serviceworker.js')
def serve_serviceworker():
    return send_from_directory('static/js', 'serviceworker.js', mimetype='application/javascript')

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('static', 'manifest.json', mimetype='application/json')

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
     return render_template('/index.html', content=dbHandler.listExtension())

@app.route('/add.html', methods=['POST', 'GET'])
def add():
	if request.method=='POST':
		email = request.form['email']
		name = request.form['name']
		dbHandler.insertContact(email,name)
		return render_template('/add.html', message="Thank you for signing up")
	else:
		return render_template('/add.html')
	
	
@app.route('/about.html', methods=['POST', 'GET'])
def about():
	return render_template('/about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
