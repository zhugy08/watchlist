from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return '<hi>Hello World</hi><img src="http://helloflask.com/totoro.gif"/>'
