from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def home():
    return "hello world"

from controller import *