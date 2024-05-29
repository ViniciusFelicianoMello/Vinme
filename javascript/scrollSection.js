// Função para rolar para uma seção com um deslocamento
document.querySelectorAll('.option_link').forEach(anchor => {
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

// Função para opção ativa em navegação
// Espera o DOM estar 100% carregado e considera visivel com 50% do viewport visivel
document.addEventListener('DOMContentLoaded', function () {
    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    }
    // função chamada sempre que entra e sai do viewport, pega ID da seção e atualiza a classe para ativa
    const callback = (entries, observer) => {
        entries.forEach(entry => {
            const id = entry.target.getAttribute('id');
            const link = document.querySelector(`.option_link[href="#${id}"]`);

            if (entry.isIntersecting) {
                document.querySelectorAll('.option_link').forEach(link => {
                    link.querySelector('.option_icon').classList.remove('option_active');
                });
                link.querySelector('.option_icon').classList.add('option_active');
            }
        });
    };
    // observa todas as seçoes da pagina
    const observer = new IntersectionObserver(callback, options);

    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });
});