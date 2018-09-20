from flask import Flask, render_template

smrh = Flask(__name__)

@smrh.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    smrh.run(debug=True, host='0.0.0.0')
