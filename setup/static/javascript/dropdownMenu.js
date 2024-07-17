document.querySelectorAll('.seta_dropdown').forEach(function(seta) {
    seta.addEventListener('click', function() {
        const menuDiv = this.closest('.dropdown_close, .dropdown_open');

        const isOpen = menuDiv.classList.contains('dropdown_open');

        document.querySelectorAll('.dropdown_open').forEach(function(openMenu) {
            openMenu.classList.remove('dropdown_open');
            openMenu.classList.add('dropdown_close');
        });

        if (isOpen) {
            menuDiv.classList.remove('dropdown_open');
            menuDiv.classList.add('dropdown_close');
        } else {
            menuDiv.classList.remove('dropdown_close');
            menuDiv.classList.add('dropdown_open');
        }
    });
});