"""
website.views script is meant for sites that can be views by users
"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user

# register views.py under Blueprint
views = Blueprint("views", __name__)

# home (pre-login) page
@views.route('/', methods=['GET', 'POST'])
def home():

    return render_template("home.html")


# dashboard (post-login) page
@views.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    
    return render_template("dashboard.html")
