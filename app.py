'''
from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return ""
@app.route('/addproduct')
def add():
    return "add"
@app.route('/removeproduct')
def remove():
    return ""
@app.route('/updateproduct')
def update():
    return ""
if __name__=="__main__":
    app.run(debug=True)
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to the Home Page</h1>"

@app.route('/addproduct')
def add():
    return "<h1>Add Product Page</h1>"

@app.route('/removeproduct')
def remove():
    return "<h1>Remove Product Page</h1>"

@app.route('/updateproduct')
def update():
    return "<h1>Update Product Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
