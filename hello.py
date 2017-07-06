# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
  message = "Hello World!"
  return render_template('index.html', message=message)

if __name__ == '__name__':
  app.debug = True
  app.run()
