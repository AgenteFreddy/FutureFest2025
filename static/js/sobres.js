function sobre_mim(){
    title = document.getElementById('title').innerHTML = 'Sobre mim'
    description = document.getElementById('descricao').innerHTML = 'Eu sou baseado na ODS “saúde e bem estar”, e vou te ajudar em sua rotina e a gerar uma imagem para você!'
    console.log('sobre_mim rodou')
}

function ODS(){
    title = document.getElementById('title').innerHTML = 'ODS'
    description = document.getElementById('descricao').innerHTML = 'Saúde e Bem-Estar, tem como missão assegurar uma vida saudável e promover o bem-estar para todas as idades, sendo essencial para o desenvolvimento sustentável.'
    console.log('ODS rodou')
}

function sobre_nos(){
    title = document.getElementById('title').innerHTML = 'Sobre Nós'
    description = document.getElementById('descricao').innerHTML = 'Somos um grupo de 5 alunos da Fiap school e desenvolvemos o projeto “Mente Estável” com o objetivo de promover a melhora da saúde mental e ajudar na visão futura da medicina'
    console.log('sobre_nos rodou')
}

function oq_acha_sobre(){
    title = document.getElementById('title').innerHTML = 'O que voce acha sobre:'
    description = document.getElementById('descricao').innerHTML = 'Como você acha que pode ser o tratamento de pessoas com problemas com questoes psicológicas?'
    console.log('oq_acha_sobre rodou')
}
setTimeout(function(){
    sobre_mim()
    console.log('sobre_mim Function rodou')
    setTimeout(function(){
        ODS()
        console.log('ODSFunction rodou')
        setTimeout(function(){
            sobre_nos()
            console.log('sobre_nosFunction rodou')
            setTimeout(function(){
                oq_acha_sobre()
                console.log('oq_acha_sobreFunction rodou')
                setTimeout(function(){
                    window.location.href = 'uresposta.html'
                    console.log('Mudou para uresposta.html')
                },5000)
            },5000)
        },5000)
    }, 5000)
})
