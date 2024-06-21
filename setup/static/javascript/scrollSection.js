// Função para rolar para uma seção com um deslocamento
document.querySelectorAll('.dropdown_link').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const sectionId = this.getAttribute('href').substring(1);
        const section = document.getElementById(sectionId);

        if (section) {
            window.scrollTo({
                top: section.offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Função para adicionar a classe 'active' ao link do dropdown correspondente
function setActiveLink() {
    const sections = document.querySelectorAll('section');
    const links = document.querySelectorAll('.dropdown_link');
    let currentActive = null;

    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top >= 0 && rect.top < window.innerHeight / 2) {
            currentActive = section.id;
        }
    });

    links.forEach(link => {
        if (link.getAttribute('href').substring(1) === currentActive) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Adiciona um EventListener para o evento de rolagem
window.addEventListener('scroll', setActiveLink);

// Chama a função uma vez ao carregar a página
setActiveLink();

// menu hamburguer fechar
document.addEventListener("DOMContentLoaded", function() {
    var menuCheckbox = document.getElementById("check-icon");
    var menuItens = document.querySelectorAll(".options_list");

    // Adiciona evento de clique a todos os itens do menu
    menuItens.forEach(function(item) {
        item.addEventListener("click", function() {
            menuCheckbox.checked = false;
        });
    });
});