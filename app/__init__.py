from flask import Flask, render_template
import os

app = Flask(__name__)

app.config['site_name'] = os.environ.get('SITE_NAME','testing')

links = [
    ['home','/',False],
    ['about','/about',False],
    ['contact','/contact',False]
]

def set_link(index):
    for itm in links:
        itm[2] = False
    links[index][2] = True
    

@app.route('/')
def index():
    set_link(0)
    return render_template('index.html',links=links,page_name='home')



@app.route('/about')
def about():
    set_link(1)
    return render_template('index.html',links=links,page_name='about')


@app.route('/contact')
def contact():
    set_link(2)
    return render_template('index.html',links=links,page_name='contact')
