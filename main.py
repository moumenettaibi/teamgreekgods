# app.py
from flask import Flask, render_template
import datetime
import time # <--- 1. ADD THIS LINE

app = Flask(__name__)

# --- This part is correct and should be kept ---
# Only set the long cache time when NOT in debug mode (i.e., for production)
# 2. CHANGE THIS BLOCK
if not app.debug:
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = datetime.timedelta(days=30)

# 3. ADD THIS NEW FUNCTION
# This function creates a 'cache_buster' variable with the current time
# and makes it available to all templates.
@app.context_processor
def inject_cache_buster():
    return dict(cache_buster=int(time.time()))


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)