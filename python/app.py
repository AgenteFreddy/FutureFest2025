from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
from openai import OpenAI
import os
import uuid
import base64

app = Flask(__name__)
CORS(app)

#criar pasta se nao existirem
if not os.path.exists('img'):
    os.makedirs('img')
if not os.path.exists('audios'):
    os.makedirs('audios')