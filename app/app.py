from flask import Flask
import os

app = Flask(__name__)

# List all items of the DynamoDB Table
@app.route("/", methods=["GET"])
def list():
    return "Hello GET"

# Get an item from the DynamoDB table
@app.route("/<name>", methods=["GET"])
def get(name):
    return "GET Hello %s" %(name)

# Post a new Item to the DynamoDB table
@app.route("/<name>", methods=["POST"])
def post(name):
    return "POST Hello %s" %(name)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')