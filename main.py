from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os
import logging
from cachetools import cached, TTLCache

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Cache with a TTL of 600 seconds (10 minutes) 
# and a maximum size of 100 items
cache = TTLCache(maxsize=100, ttl=600)

API_KEY = os.getenv('OPENAQ_KEY')

@cached(cache)
def fetch_air_quality(city):
    headers = {
        'X-API-Key': API_KEY
    }
    url = f'https://api.openaq.org/v1/latest?city={city}'
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        logging.error(f"Error fetching data from OpenAQ API: {response.status_code} - {response.text}")
        return None

    data = response.json()
    if 'results' not in data or not data['results']:
        logging.error("No results found in the API response")
        return None

    return data['results'][0]

@app.route('/air-quality', methods=['GET'])
def air_quality():
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'Please provide a city parameter'}), 400

    air_quality_data = fetch_air_quality(city)
    if not air_quality_data:
        return jsonify({'error': 'Could not retrieve air quality data'}), 500

    response_data = {
        'city': air_quality_data['city'],
        'location': air_quality_data['location'],
        'coordinates': air_quality_data['coordinates'],
        'measurements': air_quality_data['measurements']
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)