from flask import Flask, render_template, request
from scripts.api import *
from scripts.forms import WeatherForm
from os import urandom

# ------------- Init/Config -----------------
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = urandom(30)

# ------------- API ------------------
weatherapi = WeatherApi()
catapi = CatApi()
dogapi = DogApi()
# ------------- Routes ---------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=["GET", "POST"])
def weather():
    weatherform = WeatherForm()
    if request.method == "GET":
        return render_template('weather.html', form=weatherform)
    return render_template('weather.html', form=weatherform, weather=weatherapi.get_weather(request.form["city"]))

@app.route('/cat', methods=["GET"])
def cat():
    return render_template('cat.html', cat_url=catapi.get_cat())

@app.route('/dog', methods=["GET"])
def dog():
    return render_template('dog.html', dog_url=dogapi.get_dog())

# ------------- Run ------------------
if __name__ == "__main__":
    app.run(debug=True)