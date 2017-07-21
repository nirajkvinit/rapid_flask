from flask import Flask, render_template
import os, json, time, urllib.request, urllib.error, urllib.parse

app = Flask(__name__)

def get_weather():
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=London&cnt=10&mode=json&units=metric&appid=65b8831d1736fe05836815097ae4a457"
    response = urllib.request.urlopen(url).read().decode('utf8');
    return response

@app.route('/')
def index():
    data = json.loads(get_weather())
    page = "<html><head><title>My Weather</title></head><body>"
    page += "<h1>Weather for {}, {}</h1>".format(data.get('city').get('name'), data.get('city').get('country'))

    for day in data.get("list"):
        page += "<b>date:</b> {} <b>min:</b> {} <b>max:</b> {} <b>Description:</b> {} <br/>".format(
            time.strftime('%d %B', time.localtime(day.get('dt'))),
            (day.get("temp").get("min")),
            day.get("temp").get("max"),
            day.get("weather")[0].get("desctiption")
        )
        page += "</body></html>"
        return page

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
