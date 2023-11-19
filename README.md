# wiktionary_api

Simple API wrapper around wiktionaryparser library
for use with [My Wiktionary app](https://github.com/hodgeswt/Wiktionary)

## Usage
Build docker container in `sanic` folder, then run the container.

API available at `localhost:8671`: `http://localhost:8671/<lang>/<word>`

## Alternate Usage
Build docker container in `lambda` folder: `docker build --platform linux/amd64 -t wiktionary:wiktionary .`, then `docker run -p 9000:8080 wiktionary:wiktionary`

Access API via POST at `http://localhost:9000/2015-03-31/functions/function/invocations`, with POST body

```
{
    "lang": "<lang>",
    "word": "<word>"
}
```