from flask import Flask, jsonify, request, send_file
from Data.sales import DateTime, Data

Today = DateTime()
Data = Data()

app = Flask(__name__)


@app.route('/<id>', methods = ['GET', 'POST'])
def home(id):
  if request.method == 'GET':
    if id == '1':
      res = {'date': Today.date, 'time': Today.time, 'sales':Data.sales, 'revenue': Data.revenue, 'heading' : 'Every data on this page is fetch from an api call... even this text!'}
      return jsonify(res)
    elif id == '2':
      img = send_file('Data/img/out.jpg')
      img.headers.add('Access-Control-Allow-Origin', '*')
      return img
    else:
      return 'Invalid!'

if __name__ == '__main__':
  app.run(debug=True)