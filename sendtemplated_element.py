import boto3
import os
import json

from_mail = ''
to_mail = ''
template_name = ''
template_data = {'name': 'John', 'age': '27'}

ses = boto3.client(ses)
response = ses.send_templated_email(
    Source=from_mail,
    Destination={
        'ToAddresses': [
            to_mail,
        ],
    },
    Template=template_name,
    TemplateData=json.dumps(template_data)
)
print(response)
