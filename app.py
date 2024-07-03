from flask import Flask, render_template
import geocoder
from dotenv import load_dotenv
import os

# This is where you define the flask app

# Getting/loading the environment variables from .env file
load_dotenv()

# Creating a Flask instance
app = Flask(__name__)

# API key
api_key = os.getenv('API_KEY')

def home():
    return render_template('base.html')

def get_location():
    g = geocoder.ip('me')
    print(g.latlng)
