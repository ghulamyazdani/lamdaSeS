import boto3
import os
import json

ses = boto3.client('ses')

from_mail = 'cheryl.balberg@anyclip.com'
to_mail = 'anoop.gella@sager.ai'
template_name = 'AnyclipSurvey'
template_data = {'name': 'Christin Genova','email':'christine@anyclip.com','tenant':'anyclip'}

def lambda_handler(event, context):
    response = ses.send_templated_email(
    Source=from_mail,
    Destination={
        'ToAddresses': [
            'anoop.gella@sager.ai',
            'ghulam.yazdani@sager.ai',
            'vinod.verma@sager.ai',
            'ghulamyazdani12@gmail.com'
            
        ],
    },
    Template=template_name,
    TemplateData=json.dumps(template_data)
    )
    print('Email Sent')
    
    
    

