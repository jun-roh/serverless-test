# -*- coding: utf-8 -*-
import json

def run(event, context):
    response = response = {
                           "statusCode": 200,
                           "headers": {
                               "Access-Control-Allow-Origin": "*"
                           },
                           "body": None
                       }
    try:
        response['body'] = {"result" :  "Hello world"}
        print(json.dumps(response['body']))

    except Exception as err:
        # print traceback.format_exc()
        error_msg = err
        logger.error('%s\n%s', err, error_msg)
        logger.debug('%s\n%s', err, error_msg)
        if len(err.args) > 1:
            response['body'] = str(err.args[0])
            response['statusCode'] = err.args[1]
        else:
            response['body'] = '%s %s' % (type(err), str(err))
            response['statusCode'] = 500
    response['body'] = json.dumps(response['body'])

    return response
