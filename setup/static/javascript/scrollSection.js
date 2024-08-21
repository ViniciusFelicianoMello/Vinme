// Função para rolar suavemente para uma seção
document.querySelectorAll('.travel_link').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const sectionId = this.getAttribute('href').substring(1);
        const section = document.getElementById(sectionId);

        if (section) {
            section.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Função para adicionar a classe 'active' ao link do dropdown correspondente
function setActiveLink() {
    const sections = document.querySelectorAll('section');
    const links = document.querySelectorAll('.travel_link');
    let currentActive = null;

    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        const height = rect.height;
        const visiblePart = Math.max(0, Math.min(rect.bottom, window.innerHeight) - Math.max(rect.top, 0));

        if (visiblePart / height >= 0.6) {
            currentActive = section.id;
        }
    });

    if (currentActive) {
        links.forEach(link => {
            if (link.getAttribute('href').substring(1) === currentActive) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }
}

// Adiciona o evento de scroll para chamar a função setActiveLink
window.addEventListener('scroll', setActiveLink);
// Chama a função inicialmente para definir o link ativo ao carregar a página
setActiveLink();


// Adiciona o evento de scroll para chamar a função setActiveLink
window.addEventListener('scroll', setActiveLink);
// Chama a função inicialmente para definir o link ativo ao carregar a página
setActiveLink();


// // menu hamburguer fechar
// document.addEventListener("DOMContentLoaded", function() {
//     var menuCheckbox = document.getElementById("check-icon");
//     var menuItens = document.querySelectorAll(".options_list");

//     // Adiciona evento de clique a todos os itens do menu
//     menuItens.forEach(function(item) {
//         item.addEventListener("click", function() {
//             menuCheckbox.checked = false;
//         });
//     });
// });