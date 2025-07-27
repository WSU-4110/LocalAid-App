from flask import Blueprint, render_template, redirect, url_for, request, flash

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate logic here
        flash('Logged in successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Registration logic here
        flash('Registration successful!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')
