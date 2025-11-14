from flask import render_template, g, send_from_directory, abort
import sqlite3
import os
from db import get_table_name, get_db

CARDS_FOLDER = os.path.join('database', 'Cards')  # Card images folder

def card_routes(app):
    # Home page - list all cards
    @app.route('/')
    def index():
        table_name = get_table_name()  # Get the table name
        db = get_db()  # Connect to the database
        try:
            rows = db.execute(f"SELECT * FROM {table_name}").fetchall()  # Select everything from that table
        except sqlite3.OperationalError as error:
            return f"Database error: {error}"
        return render_template("index.html", cards=rows, active_page='home')

    # Card detail page
    @app.route('/card/<int:card_id>')
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

    # About page
    @app.route('/about')
    def about():
        return render_template('about.html', active_page='about')

    # Contact page
    @app.route('/contact')
    def contact():
        return render_template('contact.html', active_page='contact')

    # Decks page
    @app.route('/decks')
    def decks():
        return render_template('decks.html', active_page='decks')

    # Serve card images
    @app.route('/Cards/<path:filename>')
    def card_image(filename):
        return send_from_directory(CARDS_FOLDER, filename)
