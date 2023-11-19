import json
from wiktionaryparser import WiktionaryParser

parser = WiktionaryParser()

def lambda_handler(event, context):
    if 'lang' in event and 'word' in event:
        res = parser.fetch(event['word'], event['lang'])
    else:
        body = json.loads(event['body'])
        res = parser.fetch(body['word'], body['lang'])
    return json.dumps({'results': res})