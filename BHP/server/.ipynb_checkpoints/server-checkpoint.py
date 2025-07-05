from flask import Flask,request,jsonify
import BHP.server.utils as utils

app = Flask(__name__)

@app.route("/")
def get_location_names():
    response = jsonify({
        'locations': utils.get_locaton_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)