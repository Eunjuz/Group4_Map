from flask import Flask, render_template, request, jsonify, send_from_directory
import geopy.distance
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renders index.html from templates

@app.route('/calculate_distance', methods=['POST'])
def calculate_distance():
    data = request.get_json()  # Get JSON data from request
    points = data['points']  # Expecting points to be a list of lat/lng tuples
    total_distance = 0.0

    for i in range(1, len(points)):
        total_distance += geopy.distance.distance(points[i-1], points[i]).meters

    return jsonify({'total_distance': total_distance})

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')  # Renders homepage.html from the templates folder



if __name__ == '__main__':
    app.run(debug=True)
