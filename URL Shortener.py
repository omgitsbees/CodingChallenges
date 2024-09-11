from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound
import string
import random

app = Flask(__name__)

# Configuring SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class URLMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(8), unique=True, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Generate random short code
def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choices(characters, k=8))
    return short_code

# Home route to display instructions (GET)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the URL Shortener API. Use POST / to submit a URL for shortening.", 200

# Create shortened URL (POST)
@app.route('/', methods=['POST'])
def create_short_url():
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' field"}), 400

    long_url = data['url']
    
    # Check if URL already exists in the database
    existing_mapping = URLMapping.query.filter_by(long_url=long_url).first()
    if existing_mapping:
        return jsonify({
            "key": existing_mapping.short_code,
            "long_url": existing_mapping.long_url,
            "short_url": f"http://localhost:5000/{existing_mapping.short_code}"
        }), 200

    # Generate unique short code and save to database
    short_code = generate_short_code()
    new_mapping = URLMapping(long_url=long_url, short_code=short_code)
    db.session.add(new_mapping)
    db.session.commit()

    return jsonify({
        "key": short_code,
        "long_url": long_url,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

# Redirect shortened URL (GET)
@app.route('/<short_code>', methods=['GET'])
def redirect_to_long_url(short_code):
    mapping = URLMapping.query.filter_by(short_code=short_code).first()
    if mapping:
        return redirect(mapping.long_url, code=302)
    else:
        return jsonify({"error": "URL not found"}), 404

# Delete shortened URL (DELETE)
@app.route('/<short_code>', methods=['DELETE'])
def delete_short_url(short_code):
    mapping = URLMapping.query.filter_by(short_code=short_code).first()
    if mapping:
        db.session.delete(mapping)
        db.session.commit()
        return jsonify({"message": "URL deleted successfully"}), 200
    else:
        return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
