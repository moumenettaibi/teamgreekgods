
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the main page of the website."""
    return render_template('index.html')

@app.route('/coach')
def coach():
    """Renders the coach's profile page."""
    return render_template('coach.html')

# ADD THIS NEW ROUTE
@app.route('/faq')
def faq():
    """Renders the FAQ page."""
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)