from sanic import Sanic
from sanic.response import json
from wiktionaryparser import WiktionaryParser

app = Sanic('wiktionary_api')

parser = WiktionaryParser()

@app.route('/word/<lang>/<word>')
async def test(request, lang, word):
    res = parser.fetch(word, lang)
    return json({'results': res})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)