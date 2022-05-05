import json
import boto3

rds_client = boto3.client('rds-data')


def lambda_handler(event, context):
    response = execute_statement(
        "SELECT sager_id FROM sager_app.cust_health_history")
    return response


def execute_statement(sql):
    response = rds_client.execute_statement(
        secretArn=db_credentials_secrets_store_arn,
        database=database_name,
        resourceArn=db_cluster_arn,
        sql=sql
    )
    return response
