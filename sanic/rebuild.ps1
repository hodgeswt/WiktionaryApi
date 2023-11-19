docker stop wiktionary_api
docker remove wiktionary_api
docker build . -t wiktionary_api
docker run --name wiktionary_api -p 8000:8000 -d wiktionary_api