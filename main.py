from flask import *
from waitress import serve
import requests
import os

# Grab environment variables from docker
SHLINK_API_KEY = os.environ.get("SHLINK_API_KEY")
host = os.environ.get("host")
tag = os.environ.get("tag")

app = Flask(__name__, template_folder="templates")

@app.route('/')
def customer():
    return render_template('home.html')

@app.route('/success', methods=['POST', 'GET'])
def print_data():
    if request.method == 'POST':
        result = request.form
        longlink = result['longlink'] # User input

        # Create short link using Shlink API
        headers = {
            'Accept': "application/json",
            'Content-Type': "application/json",
            'X-Api-Key': SHLINK_API_KEY
            }
        
        json_data = {
        'longUrl': longlink,
         "tags": [
            tag
         ],
        }
        
        apiUrl = host + '/rest/v3/short-urls'
        response = requests.post(apiUrl, headers=headers, json=json_data)
        shortlink = response.json()['shortUrl']
        print("Status code:", response.status_code)
        print("Response text:", repr(response.text))

        # Return data to user
        return render_template("result.html", originallink=longlink, shortlink=shortlink)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
