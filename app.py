from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/side2')
def side2():
    return render_template('side2.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)