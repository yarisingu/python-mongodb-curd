from flask import Flask, render_template, redirect, url_for
from app.controllers.home_controller import home_blueprint


app = Flask(__name__)

# Register blueprints for different controllers
app.register_blueprint(home_blueprint)

@app.route('/')
def index():
    return redirect(url_for('home.index'))

if __name__ == '__main__':
    app.run(debug=True)
