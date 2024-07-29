document.addEventListener('DOMContentLoaded', function () {
    const carrouselItem = document.querySelector('.carrousel_item');
    const images = document.querySelectorAll('.carrousel_img');
    const prevButton = document.getElementById('prev_carrousel');
    const nextButton = document.getElementById('next_carrousel');
    let currentIndex = 0;

    // Função para atualizar a imagem principal
    function updateCarrouselItem() {
        const selectedImage = document.querySelector('.projectList_carrousel_img.selected');
        carrouselItem.style.backgroundImage = selectedImage.style.backgroundImage;
    }

    // Função para mudar a imagem selecionada
    function selectImage(index) {
        images.forEach(img => img.classList.remove('selected'));
        images[index].classList.add('selected');
        currentIndex = index;
        updateCarrouselItem();
    }

    // Adicionar evento de clique nas imagens para selecioná-las
    images.forEach((img, index) => {
        img.addEventListener('click', () => selectImage(index));
    });

    // Evento para botão "prev"
    prevButton.addEventListener('click', () => {
        let newIndex = currentIndex - 1;
        if (newIndex < 0) newIndex = images.length - 1;
        selectImage(newIndex);
    });

    // Evento para botão "next"
    nextButton.addEventListener('click', () => {
        let newIndex = currentIndex + 1;
        if (newIndex >= images.length) newIndex = 0;
        selectImage(newIndex);
    });

    // Inicializar com a primeira imagem selecionada
    selectImage(0);
});