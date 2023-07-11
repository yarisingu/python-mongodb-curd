from flask import Blueprint, render_template

# Create a blueprint for the home controller
home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/')
def index():
    return render_template('home.html')

@home_blueprint.route('/about')
def about():
    return render_template('about.html')

@home_blueprint.route('/contact')
def contact():
    return render_template('contact.html')

@home_blueprint.route('/rooms')
def rooms():
    return render_template('rooms.html')
