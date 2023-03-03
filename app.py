from flask import Flask, render_template, request, flash, session
app = Flask(__name__, template_folder="templates")#
app.secret_key = "12345"

@app.route('/hello')
def index():
    flash("what's your name?")
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    flash("Hello, " + request.form['name_input'] + " nice to meet u!")
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

