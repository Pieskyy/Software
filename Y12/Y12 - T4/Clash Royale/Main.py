from flask import Flask
from cards import card_routes
from search import search_cards
app = Flask(__name__)

# card routes for like loading cards
card_routes(app)

# Search API route
@app.route('/api/search', methods=['GET'])
def search_route():
    return search_cards()

if __name__ == '__main__':
    app.run(debug=True)