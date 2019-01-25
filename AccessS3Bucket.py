import boto3
import botocore
from datetime import tzinfo, timedelta, datetime
import datetime

# Download most recent cinema scrape from AWS S3
s3c = boto3.client('s3')
s3r = boto3.resource('s3')

Bucket = 'cinemascrape'
newscrape_file = 'newscrape.csv'

today = datetime.date.today()

get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
objs = s3c.list_objects_v2(Bucket='cinemascrape')['Contents']
[obj['Key'] for obj in sorted(objs, key=get_last_modified)]
scrapedate = objs[0]['LastModified'].date()
key = objs[0]['Key']

if scrapedate == today:
    try:
        s3r.Bucket(Bucket).download_file(key, newscrape_file)
        msg = "We got a newscrape.csv file!"
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            msg = "The scrape file does not exist in our S3 bucket."
    else:
        raise
else:
    msg = "No new cinemascrape file today"

print(msg)
