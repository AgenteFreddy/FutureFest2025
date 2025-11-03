console.log('O script esta rodando de usuarioimg.js...')
buttons = document.getElementById('buttons');
button1 = document.getElementById('button1');
button2 = document.getElementById('button2');
loading = document.getElementById('loading');
question = document.getElementById('question');
img = document.getElementById('img');
email = document.getElementById('email');
enviarDiv = document.getElementById('enviar');
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

function mandar(){
    enviar.addEventListener('click', () => {
        window.location.href = 'fim.html';
    });
}