// Função para animção apenas no viewport
function animateView() {
    var animate = document.querySelectorAll('.viewScreen');

    animate.forEach(function(cont) {
        // Verifica se pelo menos parte do view está visível e se ainda não foi animado
        if (isPartiallyInViewport(cont) && !cont.classList.contains('animado')) {
            var Destino = parseInt(cont.innerText);
            var inicio = 0;
            var Acrescimo = Math.ceil(Destino / 100); // Define o incremento

            // Função para atualizar a animação
            function atualizarAnimação() {
                inicio += Acrescimo;
                if (inicio >= Destino) {
                    cont.innerText = Destino;
                } else {
                    cont.innerText = inicio;
                    setTimeout(atualizarAnimação, 20); // Atualiza a cada 130 milissegundos
                }
            }

            atualizarAnimação();

            // Marca o elemento como animado para que não seja reiniciado
            cont.classList.add('animado');
        }
    });
}

// Adiciona um ouvinte de evento de rolagem à página para garantir que a animação seja iniciada mesmo se a seção estiver visível após o carregamento inicial
window.addEventListener('scroll', function() {
    animateView();
});

// Chama a função quando a página é carregada
window.addEventListener('load', function() {
    animateView();
});