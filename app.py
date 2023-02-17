from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime


app = Flask(__name__)
app.app_context().push()


@app.route('/')
def index():
    now = datetime.today()
    date = showDate(now.day, now.month, now.year)
    uri = "https://picsum.photos/600/600"
    return render_template('index.html', time=date, uri=uri)


def showDate(day, month, year):
    M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    suffx = suffix(day)
    date = str(day) + str(suffx) + ' ' + M[month] + ' ' + str(year)
    return date


def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')
    
if __name__ == "__main__":
    app.run(debug=True)
