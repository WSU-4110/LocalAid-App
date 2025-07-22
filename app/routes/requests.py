from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('requests', __name__)

@bp.route('/browse')
def browse():
    return render_template('browse.html')

@bp.route('/post-request', methods=['GET', 'POST'])
def post_request():
    if request.method == 'POST':
        # Save help request logic here
        flash('Your request has been posted!', 'success')
        return redirect(url_for('requests.browse'))
    return render_template('post-request.html')
