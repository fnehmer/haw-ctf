from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/challenge/<int:number>', methods=['POST'])
def verify_flag(number):
    return str(number) + str(request.data)


if __name__ == '__main__':
    app.run()
