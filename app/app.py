from hello.hello import HelloYou
import json
import datetime
import boto3
import os
import logging

from flask import Flask


import json

app = Flask(__name__)

session = boto3.session.Session()
hello = HelloYou(session, os.environ['TABLE_NAME'])

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
@app.route("/", methods=["GET"])
def healthcheck():
    return '{"health": "OK"}'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')