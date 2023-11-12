FROM sanicframework/sanic:3.8-latest

WORKDIR /sanic

COPY . .
RUN python -m pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "run.py"]