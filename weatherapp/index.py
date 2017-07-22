from flask import Flask, render_template, request
import os, json, time, urllib.request, urllib.error, urllib.parse

app = Flask(__name__)

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=10&mode=json&units=metric&appid=65b8831d1736fe05836815097ae4a457".format(city)
    response = urllib.request.urlopen(url).read().decode('utf8');
    return response

@app.route('/')
def index():
    searchcity = request.args.get("searchcity")
    if not searchcity:
        searchcity = "London"

    data = json.loads(get_weather(searchcity))

    try:
        city = data['city']['name']
    except KeyError:
        return render_template('invalid_city.html', user_input=searchcity)

    country = data['city']['country']

    forecast_list = []
    for days in data.get("list"):
        day = time.strftime("%d %B", time.localtime(days.get('dt')))
        mini = days.get("temp").get("min")
        maxi = days.get("temp").get("max")
        description = days.get("weather")[0].get("description")
        forecast_list.append((day, mini, maxi, description))
    return render_template("index.html", forecast_list=forecast_list, city=city, country=country)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
