from flask import Flask, render_template, request, jsonify
import requests

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renders index.html from templates

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    data = request.get_json()  # Expecting 'from' and 'to' coordinates
    origin = data.get('from')  # [latitude, longitude]
    destination = data.get('to')  # [latitude, longitude]

    if not origin or not destination:
        return jsonify({'error': 'Both origin and destination are required.'}), 400

    api_key = "5b3ce3597851110001cf6248b56539f5a4074fc09b0d3d9571ae8576"
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {
        "Authorization": api_key
    }
    params = {
        "start": f"{origin[1]},{origin[0]}",  # lon,lat
        "end": f"{destination[1]},{destination[0]}"  # lon,lat
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        route_data = response.json()
        distance = route_data['features'][0]['properties']['segments'][0]['distance']
        return jsonify({'distance': distance})
    else:
        return jsonify({'error': 'Failed to get route from OpenRouteService API.'}), 500

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')  # Renders homepage.html from the templates folder

if __name__ == '__main__':
    app.run(debug=True)
