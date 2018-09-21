from flask import Flask,render_template, request
from importweather import getweather

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    city = request.form.get("city")
    weathertable = getweather(city)
    return render_template('index.html',
                           weatherdata=weathertable.to_html(classes="table"),
                           city=city)


if __name__ == '__main__':
    app.run()