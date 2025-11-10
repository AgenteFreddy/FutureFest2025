from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
from openai import OpenAI
import os
import uuid
import base64
import time
import pyodbc
import smtplib
import ssl
from email.message import EmailMessage
import mimetypes

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

@app.route('/usuarioimg', methods=['POST'])
def receber_dado():
    data = request.json

    if not data:
        return jsonify({"status": "erro", "mensagem": "Nenhum dado JSON recebido"}), 400

    try:
        global usuemail_recebido

        usuemail_recebido = data['email'] 
        print(usuemail_recebido)
        if isinstance(usuemail_recebido, str):
            emailvJS = usuemail_recebido.upper()
            print(f"Email processado: {emailvJS}")
            enviar_email(usuemail_recebido) 
            
            return jsonify({
                "status": "sucesso", 
                "email_recebido": usuemail_recebido,
                "email_processado": emailvJS
            }) 

        else:
            print(f"Erro: 'email' não é uma string. Valor recebido: {usuemail_recebido}")
            return jsonify({"status": "erro", "mensagem": "O valor de 'email' deve ser uma string"}), 400

    except KeyError:
        print("Erro: Chave 'email' não encontrada no JSON")
        return jsonify({"status": "erro", "mensagem": "Chave 'email' não encontrada"}), 400
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return jsonify({"status": "erro", "mensagem": "Erro interno no servidor"}), 500


def enviar_email(user_email): 
    inemail = 'bemestarfuturefest@gmail.com' #via Email
    apppassword = os.environ.get("GMAIL_APP_PASSWORD") #app senha
    about = 'Obrigado' 
    imagem = 'img/imgchatgpt.jpg'
    body = f"""
    Olá,
    
    Obrigado por ter vindo ao nosso projeto :)
    Aqui esta a sua imagem:
    """
    
    msg = EmailMessage()
    msg['Subject'] = about
    msg['From'] = inemail 
    msg['To'] = usuemail_recebido
    msg.set_content(body)
    server_stmp = 'smtp.gmail.com'
    portal = 465
    context_ssl = ssl.create_default_context()

    ctype, encoding = mimetypes.guess_type(imagem)

    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)

    with open(imagem, 'rb') as f:
        msg.add_attachment(f.read(),
                        maintype=maintype,
                        subtype=subtype,
                        filename=os.path.basename(f.name))
        
    if not apppassword:
        print('Error the ambient GMAIL_APP_PASSWORD/app password is not defined')
    else:
        try:
            print('Conectando ao server STMP')

            with smtplib.SMTP_SSL(server_stmp, portal, context=context_ssl) as server:
                server.login(inemail, apppassword)
                print("Login realizado com sucesso.")
                
                server.send_message(msg)
                print("E-mail enviado com sucesso!")

        except smtplib.SMTPException as e:
            print(f'Error STMP ao enviar o email: {e}')
        except Exception as e:
            print(f'Ocorreu um erro inesperado:{e}')

if __name__ == '__main__':
    app.run(port=5000, debug=True)