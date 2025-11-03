from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
from openai import OpenAI
import os
import uuid
import base64
import time

client = OpenAI(
    api_key=''
)

app = Flask(__name__)
CORS(app)

#criar pasta se nao existirem
if not os.path.exists('img'):
    os.makedirs('img')
if not os.path.exists('audio'):
    os.makedirs('audio')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobres.html')
def sobres():
    return render_template('sobres.html')

@app.route('/uresposta.html')
def uresposta():
    return render_template('uresposta.html')

@app.route('/usuariosolucao.html')
def usuariosolucao():
    return render_template('usuariosolucao.html')

@app.route('/usuarioimg.html')
def usuarioimg():
    return render_template('usuarioimg.html')

@app.route('/fim.html')
def fim():
    return render_template('fim.html')

@app.route('/audio/<filename>')
def audio(filename):
    try:
        return send_file(f'audios/{filename}')
    except Exception as e:
        return f'Erro ao carregar audio: {str(e)}', 404
    
@app.route('/img')
def img_list():
    try:
        img = []
        if os.path.exists('img'):
            for filename in os.listdir('img'):
                if filename.endswith('.png'):
                    img.append({
                        'nome': filename,
                        'url': f'http://127.0.0.1:5000/img/{filename}'
                    })
        return jsonify({'img': img})
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
