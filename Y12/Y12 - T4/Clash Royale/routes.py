from flask import render_template, send_from_directory, abort
import sqlite3
import os
from blog_scraper import fetch_blog_list
from db import get_table_name, get_db
CARDS_FOLDER = os.path.join('database', 'Cards')  # Card images folder

def routes(app):
    
    @app.route('/cards') # the route to cards is different as i need my sql db to connect to it
    def cards():
        table_name = get_table_name()  # Get the table name
        db = get_db()  # Connect to the database
        try:
            rows = db.execute(f"SELECT * FROM {table_name}").fetchall()  # Select everything from that table
        except sqlite3.OperationalError as error:
            return f"Database error: {error}"
        return render_template("cards.html", cards=rows, active_page='home')

    @app.route('/card/<int:card_id>')# Card detail page, same as cards with DB connection
    def card_detail(card_id):
        table = get_table_name()
        con = get_db()
        try:
            card = con.execute(f"SELECT * FROM {table} WHERE id=?", (card_id,)).fetchone()
        except sqlite3.OperationalError as e:
            return f"Database error: {e}"
        if not card:
            abort(404)
        return render_template('card_detail.html', card=card, active_page='')

    @app.route("/")
    def index():
        return render_template("home.html", active_page='home')

    @app.route('/contact')# Contact page
    def contact():
        return render_template('contact.html', active_page='contact')

    @app.route("/blogs") # Blogs page
    def blogs_page():
        blogs = fetch_blog_list()
        return render_template("blogs.html", blogs=blogs)

    @app.route('/decks')# Decks page
    def decks():
        return render_template('decks.html', active_page='decks')

    @app.route('/Cards/<path:filename>') # Card images route
    def card_image(filename):
        return send_from_directory(CARDS_FOLDER, filename)
    
    @app.route('/serviceworker.js')
    def serve_serviceworker():
        return send_from_directory('static/js', 'serviceworker.js', mimetype='application/javascript')

