const slides = document.querySelectorAll('.slide');
const bullets = document.querySelectorAll('.bullet');
let currentIndex = 0;

bullets.forEach(bullet => {
    bullet.addEventListener('click', () => {
        currentIndex = parseInt(bullet.getAttribute('data-slide'));
        updateSlider();
    });
});

function updateSlider() {
    const offset = currentIndex * (slides[0].offsetWidth + 20);
    document.querySelector('.slider-wrapper').style.transform = `translateX(-${offset}px)`;
    document.querySelector('.bullet.active').classList.remove('active');
    bullets[currentIndex].classList.add('active');
}