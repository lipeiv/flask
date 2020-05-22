from flask import Flask
import requests

app = Flask(__name__)

@app.route("/<google_url>")
def index():
	return requests.get("https://www.google.com"+google_url).text