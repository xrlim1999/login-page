"""
Frontend page routes for the application.

Defines public and authenticated views rendered as HTML templates.
"""

from flask import Blueprint, render_template
from flask_login import login_required

# Blueprint for frontend (page-rendering) routes
views = Blueprint("views", __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    """
    Home page (pre-login)

    This page is accessible to all users and serves as the entry point
    before authentication.
    """

    return render_template("home.html")

@views.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    """
    Dashboard page (post-login).

    Requires authentication and is only accessible to logged-in users.
    """

    return render_template("dashboard.html")
