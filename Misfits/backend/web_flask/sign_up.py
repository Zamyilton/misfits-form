from flask import Flask, render_template, request, jsonify
from models.base_models import Base, session
from models.user import User

app = Flask(__name__)
app.strict_slashes=False

@app.route('/sign_up', methos=['POST'])
def sign_up():
    # retrieve sign-up details from request
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')

    # Store values with User class
    user = User(name=name, email=email, password=password)
    
    # Add updates
    session.add(user)

    # Commit changes
    session.commit()

    # Return signup message
    return jsonify('{OK}':'{Successful}'), 200


