import boto3
from botocore.exceptions import ClientError
import pymysql
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # TODO implement
    conn = pymysql.connect(host='', user='', database='',
                           password='', cursorclass=pymysql.cursors.DictCursor)
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM sager_app.cust_health_history where tenant_id= 'anyclip'")
        conn.commit()
        cur.close()
        conn.close()
    data = cur.fetchall()
    logger.info(data)
