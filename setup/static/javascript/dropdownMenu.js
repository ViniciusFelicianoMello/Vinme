document.querySelectorAll('.seta_dropdown_menu').forEach(function(seta) {
    seta.addEventListener('click', function() {
        const menuDiv = this.closest('.menu_dropdown_close') || this.closest('.menu_dropdown_open');
        
        // Verificar se o menu clicado já está aberto
        const isOpen = menuDiv.classList.contains('menu_dropdown_open');

        // Fechar todos os menus abertos
        document.querySelectorAll('.menu_dropdown_open').forEach(function(openMenu) {
            openMenu.classList.remove('menu_dropdown_open');
            openMenu.classList.add('menu_dropdown_close');
        });

        // Alternar o menu clicado
        if (menuDiv) {
            if (isOpen) {
                // Se já estava aberto, fecha
                menuDiv.classList.remove('menu_dropdown_open');
                menuDiv.classList.add('menu_dropdown_close');
            } else {
                // Se estava fechado, abre
                menuDiv.classList.remove('menu_dropdown_close');
                menuDiv.classList.add('menu_dropdown_open');
            }
        }
    });
});