from hello import HelloYou
import json
import datetime
import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# @TODO : Fix Region Name
session = boto3.session.Session(region_name="eu-west-1")
hello = HelloYou(session, os.environ['TABLE_NAME'])

# Get an item from the DynamoDB table
def get(event,context):
    name = event['pathParameters']['name']
    logger.info('Hello %s !', name)
    result = hello.get(name)
    return result

# Post a new Item to the DynamoDB table
def post(event, context):

    name = event['pathParameters']['name']
    logger.info('Hello %s !', name)
    result = hello.post(name)
    return json.dumps(result)



