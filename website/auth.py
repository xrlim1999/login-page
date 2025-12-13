from flask import Blueprint, render_template, request, flash, redirect, url_for, session, make_response
from flask_login import login_user, current_user, login_required, logout_user
from .models import User
from .constants import username_max_length, username_min_length, password_max_length, password_min_length
from . import db

auth = Blueprint("auth", __name__)

# Login
@auth.route('/login', methods=["GET", "POST"])
def login():
    # check if user is already logged-in
    if current_user.is_authenticated:
        flash("You are already logged in.", category="info")
        return redirect(url_for("views.dashboard"))
        
    # extract information
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        # check if user exists in database
        user = User.query.filter_by(username=username).first()
        if user:
            # verify input-password
            if user.check_password(password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)

                # redirect user to dashboard
                return redirect(url_for("views.dashboard"))
            
            else:
                flash("Incorrect password, please try again.", category="error")

        else:
            flash("Invalid username. Please try again or register.", category="error")

    # login attempt failed
    return render_template("login.html")

# Sign-up
@auth.route('/register', methods=["GET", "POST"])
def register():
    # extract information
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(username=username).first()

        # perform checks
        if user:
            # user already exists
            flash("Username already exists.", category="error")
            return render_template("register.html")

        # check if basic username and password criteria are met
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

        # create a new user (if checks passed)
        else:
            new_user = User(username=username)
            new_user.set_password(password1) # encrypts password into hash format
        
            # start new session
            db.session.add(new_user)
            db.session.commit()

            session['username'] = username
            # return to homepage for new_user to log in
            flash("Account successfully registered.", category="success")
            return redirect(url_for('views.home'))

    return render_template("register.html")

# Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    response = make_response(redirect(url_for("views.home")))
    response.headers["Cache-Control"] = "no-store"
    flash("Logged out successfully", category="success")
    return response