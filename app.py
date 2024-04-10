from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('homepage.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/receive')
def receive():
    return render_template('receive.html')

if __name__ == "__main__":
    app.run(debug=True)