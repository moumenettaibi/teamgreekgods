# app.py
from flask import Flask, render_template
import datetime

app = Flask(__name__)

# --- This part is correct and should be kept ---
# Tell browsers to cache static files (like CSS, JS, images) for 30 days.
# This reduces load times for repeat visitors.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = datetime.timedelta(days=30)


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