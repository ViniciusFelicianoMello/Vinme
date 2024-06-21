const botaoDark = document.getElementById('dark-mode');
const iconSun = document.querySelector('.icon-sun');
const iconMoon = document.querySelector('.icon-moon');

// Adiciona um ouvinte de evento para o evento de mudança do checkbox
botaoDark.addEventListener('change', () => {
    if (botaoDark.checked) {
        changeThemeToDark();
    } else {
        changeThemeToLight();
    }
});

// Função para alterar o tema para escuro
function changeThemeToDark() {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
    iconMoon.classList.add('visible');
    iconSun.classList.remove('visible');
}

// Função para alterar o tema para claro
function changeThemeToLight() {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    iconMoon.classList.remove('visible');
    iconSun.classList.add('visible');
}

// Verifica o tema salvo no localStorage ao carregar a página
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    botaoDark.checked = true;
    changeThemeToDark();
} else {
    botaoDark.checked = false;
    changeThemeToLight();
}