from flask import Flask, request, make_response, jsonify
import requests
import json
from geopy.geocoders import  Nominatim

app = Flask(__name__)

API_KEY = '1f538e669ad80922525da0924ecd2375'

@app.route('/')
def index():
    return 'Hello World'

def results():
    req = request.get_json(force=True)

    action = req.get('queryResult').get('action')

    result = req.get('queryResult')
    parameters = result.get('parameters')

    if parameters.get('location').get('city')