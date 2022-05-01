import boto3
from botocore.exceptions import ClientError
import pymysql


connection = pymysql.connect(
    endpoint, user=username, passwd=password, db=database_name)


def query_data():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `users`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)


def send_email():
    name = "Ghulam Yazdani"
    SENDER = "noreply@sager.ai"  # must be verified in AWS SES Email
    RECIPIENT = "ghulam.yazdani@sager.ai"  # must be verified in AWS SES Email

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-1"

    # The subject line for the email.
    SUBJECT = "This is test email for testing purpose..!!"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = (f'Hey {name}...\r\n'
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto).".format(name="ghulamYazdani")
                 )

    # The HTML body of the email.
    BODY_HTML = f"""<html>
    <head></head>
    <body>
    <h1>Hey {name}</h1>
    <p>This email was sent with
        <a href='https://aws.amazon.com/ses/'>Amazon SES CQPOCS</a> using the
        <a href='https://aws.amazon.com/sdk-for-python/'>
        AWS SDK for Python (Boto)</a>.</p>
    </body>
    </html>
                """

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {

                        'Data': BODY_HTML
                    },
                    'Text': {

                        'Data': BODY_TEXT
                    },
                },
                'Subject': {

                    'Data': SUBJECT
                },
            },
            Source=SENDER
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def lambda_handler(event, context):
    # TODO implement
    query_data()
    send_email()
