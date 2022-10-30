from doctest import debug
from flask import Flask, jsonify, request
import time

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    hour, min, sec = map(int, time.strftime("%I %M %S").split())
    if request.method == 'GET':
      data = {
          'heading' : 'Every data on this page is fetch from an api call... even this text!',
          'hour': hour,
          'min' : min,
          'sec' : sec
      }
      response = jsonify(data)
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

if __name__ == '__main__':
  app.run(debug=True)