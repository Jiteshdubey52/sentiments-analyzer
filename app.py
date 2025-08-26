
from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import csv
import os
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'change_this_to_a_random_secret_in_production'

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, 'messages.csv')

# Simple rule-based sentiment analyzer to avoid extra dependencies
POS_WORDS = set("""good great awesome amazing love like wonderful best nice happy
positive excellent fantastic pleasant enjoy fun brilliant""".split())
NEG_WORDS = set("""bad horrible terrible hate dislike worst sad angry awful
poor negative boring""".split())

def analyze_sentiment(text):
    text = text.lower()
    words = text.split()
    pos = sum(1 for w in words if w.strip('.,!?') in POS_WORDS)
    neg = sum(1 for w in words if w.strip('.,!?') in NEG_WORDS)
    score = pos - neg
    if score > 0:
        label = 'Positive'
    elif score < 0:
        label = 'Negative'
    else:
        label = 'Neutral'
    return {{'label': label, 'score': score, 'pos': pos, 'neg': neg}}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/hospital')
def project_hospital():
    return render_template('hospital.html')

@app.route('/projects/ecommerce')
def project_ecommerce():
    products = [
        {{'id':1,'name':'Eco Sneakers','price':'₹1299','desc':'Lightweight shoes','img':'/static/img/product1.jpg'}},
        {{'id':2,'name':'Smart Lamp','price':'₹899','desc':'Wi-Fi enabled lamp','img':'/static/img/product2.jpg'}},
        {{'id':3,'name':'Noise Headphones','price':'₹1999','desc':'Comfort + bass','img':'/static/img/product3.jpg'}}
    ]
    return render_template('ecommerce.html', products=products)

@app.route('/projects/sentiment', methods=['GET','POST'])
def project_sentiment():
    result = None
    text = ''
    if request.method == 'POST':
        text = request.form.get('text','')
        result = analyze_sentiment(text)
    return render_template('sentiment.html', result=result, text=text)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name','')
    email = request.form.get('email','')
    message = request.form.get('message','')
    time = datetime.utcnow().isoformat()
    # Save to CSV
    header = not os.path.exists(DATA_FILE)
    with open(DATA_FILE, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(['timestamp','name','email','message'])
        writer.writerow([time, name, email, message])
    flash('Thanks! Your message was received.')
    return redirect(url_for('index') + '#contact')

@app.route('/resume')
def resume():
    path = os.path.join(BASE_DIR, 'static', 'resume.pdf')
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

