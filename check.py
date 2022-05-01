import json
import pymysql


def lambda_handler(event, context):
    conn = pymysql.connect(host='', user='', database='',
                           password='', cursorclass=pymysql.cursors.DictCursor)
    with conn.cursor() as cur:
        cur.execute("insert into myfriends values ('firstname1','lastname1')")
        conn.commit()
        cur.close()
        conn.close()

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('data inserted')
    }
