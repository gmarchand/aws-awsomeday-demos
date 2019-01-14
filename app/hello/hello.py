import boto3
import json
import datetime
import os
import logging
import uuid 

class HelloYou():
    """Manages access to Dynamo Tables."""
    def __init__(self, session, table):
        dynamodb = session.resource('dynamodb')
        self.table = dynamodb.Table(table)
    
    def list(self):
        result = self.table.scan()
        return result['Items']
    
    def post(self,name):
        result = self.table.put_item(
        Item = {
                'name': name,
                'timestamp': datetime.datetime.utcnow().isoformat()
               } 
        )
        return result

    def get(self,name):        
        result = self.table.get_item(
            Key={
                'name': name
            }
        )
        return result['Item']
        
    