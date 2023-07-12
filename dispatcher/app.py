from dotenv import load_dotenv
from flask import Flask
from google.cloud import run
import os

load_dotenv()  # take environment variables from .env

project_id = os.environ["PROJECT_ID"]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)),
        threaded=True)