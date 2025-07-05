from flask import Flask,request,jsonify
import utils

utils.load_saved_artifacts()

app = Flask(__name__)


@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        'locations': utils.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route("/predict_home_price",methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        "estimated_price": utils.predict_estimate_price(total_sqft,location,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)