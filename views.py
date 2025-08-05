from flask import Blueprint, render_template
import json

views = Blueprint(__name__, 'views')

@views.route('/')
def index():
    with open("data.json") as f:
        projects = json.load(f)
    return render_template('home.html', projects=projects)