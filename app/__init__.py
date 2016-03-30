from flask import Flask, render_template
import os
from datetime import datetime as dt

app = Flask(__name__)

app.config['site_name'] = os.environ.get('SITE_NAME','testing')
app.config['address'] = dict(
    street=os.environ.get('ADDRESS_STREET','5555 test rd.'),
    city=os.environ.get('ADDRESS_CITY','testing city'),
    state=os.environ.get('ADDRESS_STATE','CA'),
    zipcode=os.environ.get('ADDRESS_ZIP','92804'),    
)
app.config['contact_info'] = dict(
    phone=os.environ.get('CONTACT_PHONE','(555)555-5555'),
    email=os.environ.get('CONTACT_EMAIL','test@testing.com')
)

app.jinja_env.globals['year'] = (lambda: dt.now().year)();

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
    return render_template('about.html',links=links,page_name='about')


@app.route('/contact')
def contact():
    set_link(2)
    return render_template('contact.html',links=links,page_name='contact')
