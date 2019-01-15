from hello.hello import HelloYou
from flask import Flask
import os
import boto3
import json

app = Flask(__name__)

session = boto3.session.Session(region_name="eu-west-1")
hello = HelloYou(session, 'aws-awsomeday-api-HelloTable-13QO3YN75QYQB')

# List all items of the DynamoDB Table
@app.route("/", methods=["GET"])
def list():
    result = hello.list()
    return json.dumps(result)

# Get an item from the DynamoDB table
@app.route("/<name>", methods=["GET"])
def get(name):
    result = hello.get(name)
    return json.dumps(result)

# Post a new Item to the DynamoDB table
@app.route("/<name>", methods=["POST"])
def post(name):
    result = hello.post(name)
    return json.dumps(result)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')