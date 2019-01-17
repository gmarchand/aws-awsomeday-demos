from hello.hello import HelloYou
import json
import datetime
import boto3
import os
import logging

from flask import Flask


import json

app = Flask(__name__)

# TODO : Fix Region Name
session = boto3.session.Session(region_name="eu-west-1")
# TODO : Fix table name to env var.
hello = HelloYou(session, 'aws-awsomeday-api-HelloTable-13QO3YN75QYQB')

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