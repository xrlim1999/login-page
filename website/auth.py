"""
Authentication routes for the application.

Handles user login, registration, and logout, 
including credential validation, session authentication, and redirects.
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for, session, make_response
from flask_login import login_user, current_user, login_required, logout_user
from .models import User
from .constants import username_max_length, username_min_length, password_max_length, password_min_length
from . import db

# Blueprint for frontend (page-rendering) routes
auth = Blueprint("auth", __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    """
    Logs in the user after validating the username and password.
    """
    # redirect logged-in users to dashboard
    if current_user.is_authenticated:
        flash("You are already logged in.", category="info")
        return redirect(url_for("views.dashboard"))
        
    if request.method == "POST":
        # extract user credentials from form
        username = request.form.get('username')
        password = request.form.get('password')

        # validation: empty fields
        if not username or not password:
            flash("Please make sure that no fields are empty.", category="error")
            return render_template("login.html")

        # retrieve user from database
        user = User.query.filter_by(username=username).first()
        if user:
            if user.check_password(password):
                # authentication - successful
                login_user(user, remember=True)
                flash("Logged in successfully!", category="success")
                return redirect(url_for("views.dashboard"))
            else:
                # password - failed
                flash("Incorrect password, please try again.", category="error")
        else:
            # username - failed
            flash("Invalid username. Please try again or register.", category="error")

    return render_template("login.html") # login attempt failed

@auth.route('/register', methods=["GET", "POST"])
def register():
    """
    Registers new user's information.
    Ensures all provided information meet the pre-requisites.
    """
    if request.method == "POST":
        # extract user credentials from form
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # validation: empty fields
        if not username or not password1 or not password2:
            flash("Please make sure that no fields are empty.", category="error")
            return render_template("register.html")

        # retrieve user from database
        user = User.query.filter_by(username=username).first()
        if user:
            # user already exists
            flash("Username already exists.", category="error")
            return render_template("register.html")

        # username and password criteria must be met
        elif len(username) < username_min_length:
            flash(f"Username must be at least {username_min_length} characters long.", category="error")
        elif len(username) > username_max_length:
            flash(f"Username must be no more than {username_max_length} characters long.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < password_min_length:
            flash(f"Password must be at least {password_min_length} characters long.", category="error")
        elif len(password1) > password_max_length:
            flash(f"Password must be no more than {password_max_length} characters long.", category="error")

        else:
            # create a new user (registration - successful)
            new_user = User(username=username)
            new_user.set_password(password1)
        
            # persist the new user to database
            db.session.add(new_user)
            db.session.commit()
            flash("Account successfully registered. Please log in to continue.", category="success")
            
            return redirect(url_for('auth.login'))

    return render_template("register.html")

@auth.route('/logout')
@login_required
def logout():
    """
    Log the current user out and invalidate the session.
    Redirects to the home page after logout.
    """
    logout_user()

    # prevent cached authenticated pages
    response = make_response(redirect(url_for("views.home")))
    response.headers["Cache-Control"] = "no-store"

    flash("Logged out successfully", category="success")
    return response