from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('OPENAQ_KEY')

@app.route('/air-quality', methods=['GET'])
def air_quality():
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'Please provide a city parameter'}), 400
    
    headers = {
        'X-API-Key': API_KEY
    }

    url = f'https://api.openaq.org/v1/latest?city={city}'
    response = requests.get(url, headers=headers)

    data = response.json()

    if 'results' not in data or not data['results']:
        return jsonify({'error': 'Could not retrieve air quality data'}), 500

    air_quality_data = {
        'city': data['results'][0]['city'],
        'location': data['results'][0]['location'],
        'measurements': data['results'][0]['measurements']
    }

    return jsonify(air_quality_data)

if __name__ == '__main__':
    app.run(debug=True)