import boto3
import os
import json
import boto3
import csv

key = 'anyclip/nps-data/survey.csv'
bucket = 'glue-studio-sager'
s3_resource = boto3.resource('s3')
s3_object = s3_resource.Object(bucket, key)

data = s3_object.get()['Body'].read().decode('utf-8').splitlines()

lines = csv.reader(data)
headers = next(lines)
print('headers: %s' % (headers))


ses = boto3.client('ses')

from_mail = 'cheryl.balberg@anyclip.com'


template_data = {'name': 'Christin Genova',
                 'email': 'christine@anyclip.com', 'tenant': 'anyclip'}


def lambda_handler(event, context):
    for line in lines:
        to_mail = line[1]
        template_name = 'AnyclipSurvey'
        template_data = {'name': line[0],
                         'email': line[1], 'tenant': 'anyclip'}
        response = ses.send_templated_email(
            Source=from_mail,
            Destination={
                'ToAddresses': [
                    to_mail
                ],
            },
            Template=template_name,
            TemplateData=json.dumps(template_data)
        )
    print('Email Sent')
    # print complete line
    print(line)
    # print index wise
    print(line[0], line[1])
