from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/faq')
def faq():
    return render_template('faq.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/privacy')
def privacy():
    return render_template('privacy.html')
