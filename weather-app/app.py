from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None

    if request.method == 'POST':
        city = request.form['city']

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        data = response.json()

        weather = {
            'city': city,
            'temperature': data['current_condition'][0]['temp_C'],
            'description': data['current_condition'][0]['weatherDesc'][0]['value']
        }

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)