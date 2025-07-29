from flask import Blueprint, render_template_string, request, redirect, url_for, flash

bp = Blueprint('requests', __name__)


BROWSE_TEMPLATE = """
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    {% for category, message in messages %}
      <div class="flash {{ category }}">{{ message }}</div>
    {% endfor %}
  {% endif %}
{% endwith %}
<h1>Browse Help Requests</h1>
"""
POST_TEMPLATE = """
<form method='post'>
    <input type='submit' value='Post Request'>
</form>
"""

@bp.route('/browse')
def browse():
    
    return render_template_string(BROWSE_TEMPLATE)

@bp.route('/post-request', methods=['GET', 'POST'])
def post_request():
    if request.method == 'POST':
        
        flash('Your request has been posted!', 'success')
        return redirect(url_for('requests.browse'))
    return render_template_string(POST_TEMPLATE)