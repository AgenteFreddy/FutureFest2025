console.log('O script esta rodando de usuarioimg.js...')
buttons = document.getElementById('buttons');
button1 = document.getElementById('button1');
button2 = document.getElementById('button2');
loading = document.getElementById('loading');
question = document.getElementById('question');
img = document.getElementById('img');
email = document.getElementById('email');
enviarDiv = document.getElementById('enviar');
mandarid =  document.getElementById('mandarid');

setTimeout(function(){
    console.log('setTimeout Rodou...')
    buttons.style.display = 'block'
    question.style.display = 'block'
    img.style.width = '300px'
},5000)


function start(){
    email.style.display = 'block'
    document.getElementById('question').innerHTML = 'Adicione seu email'
    buttons.style.display = 'none'
    enviarDiv.style.display = 'block'
}

function finish(){
    button2.addEventListener('click', () => {
        window.location.href = 'fim.html';
    });  
}

function mandar() {
    mandarid.disabled = true
    enviarDiv.addEventListener('click', async () => {
        
        const emailParaEnviar = document.getElementById('email').value;
        if (!emailParaEnviar) {
            alert('Por favor, digite seu email.');
            return;
        }

        console.log(`Enviando email: ${emailParaEnviar} para o Python...`);
        const dados = {
            email: emailParaEnviar
        };

        try {
            const response = await fetch('http://127.0.0.1:5000/usuarioimg', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dados)
            });
            const respostaDoServidor = await response.json();

            console.log('Resposta do Python:', respostaDoServidor);

            if (respostaDoServidor.status === "sucesso") {
                console.log('Dados recebidos pelo servidor. Redirecionando...');
                window.location.href = 'fim.html';
            } else {
                alert(`Erro do servidor: ${respostaDoServidor.mensagem}`);
            }

        } catch (error) {
            console.error('Erro ao conectar com o servidor:', error);
            alert('Não foi possível conectar ao servidor. Verifique o console.');
        }
    });
}