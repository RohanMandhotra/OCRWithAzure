from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def home():
    return render_template('pages/index.html')

