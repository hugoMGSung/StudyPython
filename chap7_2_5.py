from urllib import request
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(target, "html.parser")
    output = ""
    for item in soup.select("location"):
        output += "<h3>{}</h3>".format(item.select_one("city").string)
        output += "<p>날씨: {}</p>".format(item.select_one("wf").string)
        output += "최저/최고기온: {}℃ / {}℃ ".format( \
            item.select_one("tmn").string, \
            item.select_one("tmx").string)
        output += "<hr/>"
    return output

app.run('127.0.0.1', debug=False)

