from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'bengaluru'  # Default city
    api = "a6ce74fdc6cd7a7d4f5716bb824afa05"

    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
        source = urllib.request.urlopen(url).read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(round(list_of_data['main']['temp'] - 273.15, 2)) + '°C',
            "pressure": str(list_of_data['main']['pressure']) + ' hPa',
            "humidity": str(list_of_data['main']['humidity']) + '%',
        }
        print(data)
    except Exception as e:
        data = None
        error = "City not found or API error occurred. Please try again."
        return render_template('index.html', error=error)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

