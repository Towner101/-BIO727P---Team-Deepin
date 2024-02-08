from flask import Blueprint, render_template

#define the name of the Blueprint
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('base.html')