from flask import render_template, request


from app import app

@app.route('/')
@app.route('/index')
def initialpage():
    return render_template('index.html', title='Home Page')

@app.route('/joinus')
def charts():
    return render_template('joinus.html', title='Charts')

@app.route('/register', methods=['POST', 'GET'])
def getForm():
    name = request.form['name']
    born = request.form['born']
    nationality = request.form['nationality']
    email = request.form['email']
    phone = request.form['phone']
    description = request.form['description']
    skills = request.form['skills']
    experience = request.form['experience']

    json =
    print(name, born, nationality, email, phone, description, skills, experience)

    return render_template('register.html', title='Register')
