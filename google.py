from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return requests.get("https://www.google.com")