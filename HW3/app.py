from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/profile', methods=['POST'])
def profile():
    fname = request.form['firstname']
    lname = request.form['lastname']
    sex = request.form['sex']
    status = request.form['status']
    location = request.form['location']
    
    return render_template(
        'profile.html',
        firstname=fname,
        lastname=lname,
        sex=sex,
        status=status,
        location=location
    )

if __name__ == '__main__':
    app.run(debug=True)
