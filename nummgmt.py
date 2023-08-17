from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    aggregated_numbers = []

    for url in urls:
        try:
            response = requests.get(url)
            response_data = response.json()
            if "numbers" in response_data and isinstance(response_data["numbers"], list):
                aggregated_numbers.extend(response_data["numbers"])
        except (requests.exceptions.RequestException, ValueError):
            pass  # Handle errors here if needed

    response_json = {"numbers": aggregated_numbers}
    return jsonify(response_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
