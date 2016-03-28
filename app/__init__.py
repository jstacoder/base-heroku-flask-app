from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',links=[['home','/',True],['about','/about',False],['contact','/contact',False]],page_name='home')



@app.route('/about')
def about():
    return render_template('index.html',links=[['home','/',False],['about','/about',True],['contact','/contact',False]],page_name='about')


@app.route('/contact')
def contact():
    return render_template('index.html',links=[['home','/',False],['about','/about',False],['contact','/contact',True]],page_name='contact')
