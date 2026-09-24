
from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b

@app.route('/')
def home():
    return "Hello, mera pehla live app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
