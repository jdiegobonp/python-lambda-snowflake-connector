import snowflake.connector
import json

SNOW_ACCOUNT = '<Format XSXSXSX-OOXX0000>' 
SNOW_USER = '<User>'
SNOW_PASS = '<Password>'
SNOW_FILE_FORMAT = 'DEFAULT_CSV'
SNOW_DB = '<db name>'
SNOW_SCHEMA = 'CORE'

def lambda_handler(event, context):
    # connect to snowflake - set ocsp response cache to /tmp, the only place we can write on lambda
    ctx = snowflake.connector.connect(
        user=SNOW_USER,
        password=SNOW_PASS,
        account=SNOW_ACCOUNT,
        database=SNOW_DB,
        schema=SNOW_SCHEMA
        )
    cs = ctx.cursor()

    # load the scored file
    # add your own error handling
    try:
        cs.execute("SELECT current_version()")
        one_row = cs.fetchone()
        print(one_row[0])
    
    finally:
        cs.close()
    ctx.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps(one_row)
    }
