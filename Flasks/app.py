# app.py
from flask import Blueprint, Flask, render_template, request, flash, redirect, url_for
from flask import current_app as ca

# Flask 객체 인스턴스 생성
app = Flask(__name__)
# Blueprint 객체 인스턴스 생성
#app = Blueprint('main', __name__, url_prefix='/')

@app.route('/') # 접속 url
def index():
    testData = 'TestData Array'
    #return render_template('index.html', user='휴고', data={'level':99, 'point':360, 'exp':45000})
    return render_template('test.html', testDataHtml=testData)

if __name__ == '__main__':
    app.run(debug=True)