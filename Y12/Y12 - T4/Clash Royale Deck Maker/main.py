from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler
from flask import send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/db_images/<path:subpath>')
def db_image(subpath):
    # Expect DB values like "cards/archers.png"
    # reject traversal and absolute paths
    if '..' in subpath or subpath.startswith(('/', '\\')):
        abort(404)
    base_dir = os.path.join(app.root_path, 'Database')
    full_path = os.path.normpath(os.path.join(base_dir, subpath))
    # ensure resolved path stays inside Database
    if not full_path.startswith(os.path.normpath(base_dir) + os.sep):
        abort(404)
    folder, filename = os.path.split(subpath)
    serve_dir = os.path.join(base_dir, folder) if folder else base_dir
    return send_from_directory(serve_dir, filename)

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
