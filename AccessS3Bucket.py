#!/usr/bin/python3.6

import boto3
import botocore
from datetime import tzinfo, timedelta, datetime
import datetime
from email.message import EmailMessage
import smtplib

# Who gets the email
receiver = ['doug.ray@starbanner.com']

# Which market is reported
market = 'Gainesville and Ocala, for now'

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

# SEND REPORT to recipient(s).
#with open(bigreport) as fp:
# Create a text/plain message
msg = EmailMessage()
msg.set_content("No content yet")

sender = 'data@sunwriters.com'
gmail_password = '%WatchingTheDetectives'
msg['Subject'] = f'Latest cinema scrape for {market}'
msg['from'] = sender
msg['To'] = receiver

# Send the message via our own SMTP server.
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender, gmail_password)
    server.send_message(msg)
    server.quit()
except:
    print('Something went wrong...')