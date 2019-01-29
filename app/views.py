from flask import render_template, request


from app import app

@app.route('/')
@app.route('/index')
def initialpage():
    return render_template('index.html', title='Home Page')

@app.route('/joinus')
def charts():
    return render_template('joinus.html', title='Charts')