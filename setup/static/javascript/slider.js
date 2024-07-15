let items = document.querySelectorAll('.slider .slider_card');
let active = 0;

// função para retornar o valor comforme a largura da tela
function getTranslateXValue(stt) {
    if (window.matchMedia("(max-width: 600px)").matches) {
        return `${65 * stt}vw`;
    } else if (window.matchMedia("(max-width: 1024px)").matches) {
        return `${48 * stt}vw`;
    } else {
        return `${26 * stt}vw`;
    }
}

//função para carregar o slider
function loadShow() {
    items[active].style.transform = `none`;
    items[active].style.zIndex = 1;

    let stt = 0;
    for (let i = active + 1; i < items.length; i++) {
        stt++;
        items[i].style.transform = `translateX(${getTranslateXValue(stt)}) scale(${1 - 0 * stt})`;
        items[i].style.zIndex = -stt;
    }

    stt = 0;
    for (let i = active - 1; i >= 0; i--) {
        stt++;
        items[i].style.transform = `translateX(${getTranslateXValue(-stt)}) scale(${1 - 0 * stt})`;
        items[i].style.zIndex = -stt;
    }

    updateBullets();
}

loadShow();

let next = document.getElementById('next');
let prev = document.getElementById('prev');

next.onclick = function () {
    active = active + 1 < items.length ? active + 1 : active;
    loadShow();
};

prev.onclick = function () {
    active = active - 1 >= 0 ? active - 1 : active;
    loadShow();
};

// função para atualizar os bullets
function updateBullets() {
    const bulletsContainer = document.querySelector('.bullets');
    bulletsContainer.innerHTML = '';

    items.forEach((item, index) => {
        const bullet = document.createElement('span');
        bullet.classList.add('bullet');
        if (index === active) {
            bullet.classList.add('active');
        }
        bullet.addEventListener('click', () => {
            active = index;
            loadShow();
        });
        bulletsContainer.appendChild(bullet);
    });
}