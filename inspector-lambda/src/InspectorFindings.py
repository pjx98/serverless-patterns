import json
import boto3
from datetime import datetime
import os

S3_BUCKET = os.environ['S3_BUCKET']

s3 = boto3.resource('s3')
bucket = s3.Bucket(S3_BUCKET)


def handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    finding = event

    #print("From EventBridge: " + str(finding))

    todays_date = format_date(datetime.today())
        
    write_to_s3(finding, todays_date)

    return finding
    
# Save JSON data file to S3
def write_to_s3(finding, todays_date):
    
    event_id = finding['id']
    
    filePath = todays_date
    
    response = bucket.put_object(
        Body = json.dumps(finding).encode('UTF-8'),
        Key = f'findings/{filePath}/{event_id}.json'
    )

    return response
    
# Return a date with format YYYY-MM-DD
def format_date(date_object):

    formatted_date = date_object.strftime('%Y/%m/%d/%H/%M')

    return formatted_date