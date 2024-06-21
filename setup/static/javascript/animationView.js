// Função para verificar se o elemento está visível na tela
function isElementInViewport(el, margin) {
    var rect = el.getBoundingClientRect();
    return (
        rect.bottom >= - margin &&
        rect.right >= 0 &&
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.left <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Função para lidar com o evento de rolagem
function handleScroll() {
    var animationElements = document.querySelectorAll('.viewport');
    animationElements.forEach(function(element) {
        if (isElementInViewport(element, 100)) {
            element.classList.add('visible');
            } else {
        }
    });
}

window.addEventListener('scroll', handleScroll);
handleScroll();