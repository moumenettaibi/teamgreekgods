# app.py
from flask import Flask, render_template
from flask_talisman import Talisman
from flask_compress import Compress
import datetime
import time

app = Flask(__name__)
Compress(app)

# ==================== Security Configuration ====================
# Define a Content Security Policy (CSP)
csp = {
    'default-src': "'self'",
    'style-src': [
        "'self'",
        "https://fonts.googleapis.com",
        "'unsafe-inline'"  # Required for inline styles
    ],
    'font-src': [
        "'self'",
        "https://fonts.gstatic.com"
    ],
    'img-src': [
        "'self'",
        "https://i.ytimg.com",
        "data:",
        "https://play.google.com",
        "https://developer.apple.com"
    ],
    'script-src': [
        "'self'",
        "'unsafe-inline'"  # Required for inline scripts
    ],
    'frame-src': [
        "'self'",
        "https://www.youtube.com"
    ],
    'object-src': "'none'",
    'base-uri': "'self'",
    'form-action': "'self'",
    'frame-ancestors': "'none'"
}

# Initialize Talisman with the app and the CSP
# force_https=False because SSL is handled by the hosting provider (e.g., Vercel)
Talisman(app, content_security_policy=csp, force_https=False)

# ==================== Cache Busting ====================
# Set a long cache time for static files in production
if not app.debug:
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = datetime.timedelta(days=1220)

# This function creates a 'cache_buster' variable with the current time
# and makes it available to all templates.
@app.context_processor
def inject_cache_buster():
    """Injects a cache-busting variable into all templates."""
    return dict(cache_buster=int(time.time()))

# ==================== App Routes ====================
@app.route('/')
def home():
    """Renders the main page of the website."""
    return render_template('index.html')

@app.route('/coach')
def coach():
    """Renders the coach's profile page."""
    return render_template('coach.html')

@app.route('/faq')
def faq():
    """Renders the FAQ page."""
    return render_template('faq.html')

@app.route('/calculator')
def calculator():
    """Renders the fitness calculator page."""
    return render_template('calculator.html')

# ==================== Startup ====================
# This block is for local development only.
# For production, a WSGI server like Gunicorn should be used.
# Example: gunicorn --config gunicorn_config.py main:app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4343, debug=True)