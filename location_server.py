from flask import Flask, request

app = Flask(__name__)

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(f"Received location: Latitude: {latitude}, Longitude: {longitude}")
    # Here you can integrate with your AI model or perform actions based on the location
    return "Location received!", 200

if __name__ == '__main__':
    app.run(port=5000)
