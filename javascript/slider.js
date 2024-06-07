const slides = document.querySelectorAll('.slide');
const bullets = document.querySelectorAll('.bullet');
let currentIndex = 0;

// Para cada bullet um evento de click que atualiza o valor do atributo data-slide do bullet clickado
bullets.forEach(bullet => {
    bullet.addEventListener('click', () => {
        currentIndex = parseInt(bullet.getAttribute('data-slide'));
        updateSlider();
    });
});

// função calcula o deslocamento em pixels com base na largura do primeiro slide, atualiza o translateX, remove e adiciona a classe active
function updateSlider() {
    const offset = currentIndex * (slides[0].offsetWidth + 10);
    document.querySelector('.slider-wrapper').style.transform = `translateX(-${offset}px)`;
    document.querySelector('.bullet.active').classList.remove('active');
    bullets[currentIndex].classList.add('active');
}