# fourth Hello World program

# uses pipenv requests

__author__ = 'whil'

print('Hello World for the Fourth Time')

import requests
response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))


from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World, from Flask, AGAIN!</h1>'

if __name__ == '__main__':
    app.run(debug=True)


