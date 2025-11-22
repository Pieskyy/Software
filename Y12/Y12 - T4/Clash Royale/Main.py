from flask import Flask
from routes import routes
from search import search_cards
app = Flask(__name__)

routes(app)# card routes for like loading cards aswell as links to pages

@app.route('/api/search', methods=['GET']) # searching
def search_route():
    return search_cards()

if __name__ == '__main__':
    app.run(debug=True)