import hello
import uuid
import json
import boto3
from hello import HelloYou

name = str(uuid.uuid1())
print('Name:',name)
session = boto3.session.Session()
hello = HelloYou(session, 'aws-awsomeday-api-HelloTable-13QO3YN75QYQB')
result = hello.post(name)
print(json.dumps(result))
result = hello.get(name)
print(json.dumps(result))
result = hello.list()
print(json.dumps(result))